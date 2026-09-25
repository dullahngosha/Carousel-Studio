from __future__ import annotations
import argparse, json, os, random
from pathlib import Path
from .asset_registry import production_assets
from .comfy_client import ComfyClient
from .prompt_guard import sanitize_scene_prompt
from .workflow_adapter import prepare_workflow, enforce_single_image
from .pipeline import build_jobs
from .render_manifest import write_manifest

def render(plan, workflow_path="workflows/scene-api.json", output_root="outputs", dry_run=False):
    assets=production_assets()
    jobs=build_jobs(plan,output_root)
    write_manifest(Path(plan).stem,jobs,assets,Path(output_root)/"manifest.json")
    if dry_run:
        return jobs
    client=ComfyClient(os.getenv("COMFYUI_URL","http://127.0.0.1:8188"))
    template=client.load_workflow(workflow_path)
    neg_master=Path("prompts/NEGATIVE_MASTER.txt").read_text(encoding="utf-8").strip()
    results=[]
    for job in jobs:
        positive=sanitize_scene_prompt(job["prompt"])
        negative=", ".join(x for x in [neg_master,job.get("negative_prompt","")] if x)
        wf=prepare_workflow(template,positive,negative,random.randrange(1,2**63-1))
        enforce_single_image(wf)
        pid=client.queue(wf)
        history=client.wait(pid)
        results.append({"slide_id":job["slide_id"],"prompt_id":pid,"history":history})
    return results

if __name__=="__main__":
    ap=argparse.ArgumentParser(description="Render 15 independent carousel scenes")
    ap.add_argument("plan")
    ap.add_argument("--workflow",default="workflows/scene-api.json")
    ap.add_argument("--output-root",default="outputs")
    ap.add_argument("--dry-run",action="store_true")
    a=ap.parse_args()
    print(json.dumps(render(a.plan,a.workflow,a.output_root,a.dry_run),ensure_ascii=False,indent=2))
