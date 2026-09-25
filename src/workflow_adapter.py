from __future__ import annotations
import copy

class WorkflowTemplateError(RuntimeError): pass

def inject(workflow, positive, negative, seed, filename_prefix):
    """
    Template contract:
      node title CAROUSEL_POSITIVE -> CLIPTextEncode
      node title CAROUSEL_NEGATIVE -> CLIPTextEncode
      node title CAROUSEL_SEED -> sampler with inputs.seed
      node title CAROUSEL_SAVE -> SaveImage
    """
    wf=copy.deepcopy(workflow)
    found=set()
    for node_id,node in wf.items():
        title=node.get("_meta",{}).get("title","")
        inputs=node.setdefault("inputs",{})
        if title=="CAROUSEL_POSITIVE": inputs["text"]=positive; found.add(title)
        elif title=="CAROUSEL_NEGATIVE": inputs["text"]=negative; found.add(title)
        elif title=="CAROUSEL_SEED": inputs["seed"]=int(seed); found.add(title)
        elif title=="CAROUSEL_SAVE": inputs["filename_prefix"]=filename_prefix; found.add(title)
    required={"CAROUSEL_POSITIVE","CAROUSEL_NEGATIVE","CAROUSEL_SEED","CAROUSEL_SAVE"}
    missing=required-found
    if missing: raise WorkflowTemplateError("Workflow missing tagged nodes: "+", ".join(sorted(missing)))
    return wf
