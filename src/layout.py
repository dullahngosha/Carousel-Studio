from __future__ import annotations
CANVAS_W,CANVAS_H=1080,1350
SAFE=64
LOGO_BOX=(866,52,1016,202)
HEADLINE_BOX=(64,64,820,300)
BODY_BOX=(64,300,1016,1110)
FOOTER_BOX=(0,1240,1080,1350)

def validate_box(box):
    x1,y1,x2,y2=box
    return 0<=x1<x2<=CANVAS_W and 0<=y1<y2<=CANVAS_H

def spec():
    boxes={"logo":LOGO_BOX,"headline":HEADLINE_BOX,"body":BODY_BOX,"footer":FOOTER_BOX}
    assert all(validate_box(v) for v in boxes.values())
    return {"canvas":[CANVAS_W,CANVAS_H],"safe_margin":SAFE,"boxes":boxes}
