from pathlib import Path
import shutil
from .qc import inspect_image

def export(slide_files,out="deliverables"):
    if len(slide_files)!=15: raise ValueError("Expected exactly 15 separate slide files")
    root=Path(out); b1=root/"batch-01"; b2=root/"batch-02"
    b1.mkdir(parents=True,exist_ok=True); b2.mkdir(parents=True,exist_ok=True)
    outputs=[]
    for i,src in enumerate(slide_files,1):
        inspect_image(src)
        dst=(b1 if i<=10 else b2)/f"slide-{i:02d}.png"
        shutil.copy2(src,dst); outputs.append(str(dst))
    if len(list(b1.glob("*.png")))!=10: raise RuntimeError("Batch 01 must contain exactly 10 PNGs")
    if len(list(b2.glob("*.png")))!=5: raise RuntimeError("Batch 02 must contain exactly 5 PNGs")
    return outputs
