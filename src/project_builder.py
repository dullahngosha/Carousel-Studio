from __future__ import annotations
import json
from pathlib import Path
from .prompt_guard import sanitize_scene_prompt
from .validate_plan import validate_slide_plan

def build_project(article:str, slides:list[dict], out_dir="projects/current"):
    validate_slide_plan(slides)
    root=Path(out_dir); root.mkdir(parents=True,exist_ok=True)
    (root/"source.txt").write_text(article,encoding="utf-8")
    clean=[]
    for s in slides:
        x=dict(s)
        x["image_prompt"]=sanitize_scene_prompt(x["image_prompt"])
        clean.append(x)
    (root/"plan.json").write_text(json.dumps(clean,ensure_ascii=False,indent=2),encoding="utf-8")
    return root
