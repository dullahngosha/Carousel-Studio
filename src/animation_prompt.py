from pathlib import Path
MASTER=Path("prompts/ANIMATION_MASTER.md")
def for_slide(scene_notes=""):
    base=MASTER.read_text(encoding="utf-8")
    return base+"\n\nScene-specific allowed motion:\n"+scene_notes.strip()+"\n"
