from __future__ import annotations

from pathlib import Path

def split_batches(slides: list[dict]) -> list[list[dict]]:
    if len(slides) != 15:
        raise ValueError("Carousel Studio currently expects exactly 15 slides.")
    return [slides[:10], slides[10:]]

def output_path(root: str | Path, slide_id: int) -> Path:
    root = Path(root)
    batch = "batch-01" if slide_id <= 10 else "batch-02"
    return root / batch / f"slide-{slide_id:02d}.png"
