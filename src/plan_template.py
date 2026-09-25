import json
from pathlib import Path
def create(topic,output="plans/new-carousel.json"):
    slides=[{"id":i,"headline":"","support_text":"","scene":"","subjects":[],"image_prompt":f"ONE complete standalone vertical 4:5 scene about {topic}, one coherent environment, one main visual story","negative_prompt":"collage, grid, contact sheet, montage, multi-panel, split screen, multiple slides, tiled layout"} for i in range(1,16)]
    p=Path(output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(slides,indent=2,ensure_ascii=False),encoding="utf-8"); return p
