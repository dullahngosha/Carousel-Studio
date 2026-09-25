from __future__ import annotations

FORBIDDEN = (
    "collage",
    "grid",
    "contact sheet",
    "multi-panel",
    "multipanel",
    "split screen",
    "multiple slides",
    "tiled layout",
    "2x2",
    "3x3",
)

def validate_prompt(prompt: str) -> None:
    lower = prompt.lower()
    hits = [term for term in FORBIDDEN if term in lower]
    if hits:
        raise ValueError(
            "Prompt rejected by ONE SLIDE = ONE IMAGE policy. "
            f"Forbidden terms found: {', '.join(hits)}"
        )

def validate_slide_plan(slides: list[dict], expected: int = 15) -> None:
    if len(slides) != expected:
        raise ValueError(f"Expected {expected} slides, got {len(slides)}")

    seen = set()
    for slide in slides:
        sid = slide.get("id")
        if sid in seen:
            raise ValueError(f"Duplicate slide id: {sid}")
        seen.add(sid)

        prompt = slide.get("image_prompt", "")
        if not prompt.strip():
            raise ValueError(f"Slide {sid} has no image prompt")
        validate_prompt(prompt)
