from __future__ import annotations
import re

FORBIDDEN_PATTERNS=[
 r"\bcollage\b",r"\bcontact sheet\b",r"\bmulti[- ]?panel\b",
 r"\bsplit[- ]?screen\b",r"\bgrid of\b",r"\bmultiple slides\b",
 r"\b2\s*[x×]\s*2\b",r"\b3\s*[x×]\s*3\b",r"\btiled layout\b"
]

MANDATORY_PREFIX=(
 "Create exactly ONE complete standalone vertical 4:5 image, 1080x1350. "
 "One main scene only. Do not create a collage, grid, contact sheet, split screen, "
 "multi-panel composition, montage, or multiple slides in one image. "
)

def sanitize_scene_prompt(prompt:str)->str:
    clean=" ".join(prompt.split())
    hits=[p for p in FORBIDDEN_PATTERNS if re.search(p,clean,re.I)]
    if hits: raise ValueError("Unsafe carousel composition instruction detected.")
    return MANDATORY_PREFIX+clean

def negative_prompt(extra="")->str:
    base=(
      "collage, grid, contact sheet, montage, multi-panel, split screen, multiple slides, "
      "tiled composition, slide number, generated typography, generated logo, watermark, "
      "face drift, duplicate person, extra fingers, extra limbs, malformed hands"
    )
    return base+(", "+extra.strip() if extra.strip() else "")
