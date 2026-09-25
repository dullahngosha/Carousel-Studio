from __future__ import annotations
from pathlib import Path
import hashlib, yaml

REQUIRED_ASSETS = {
    "official_logo": "assets/official/immigration-logo.png",
    "nyanzobe": "assets/references/nyanzobe.png",
    "mbitiyaza": "assets/references/mbitiyaza.png",
}

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def check(root="."):
    root=Path(root)
    report={"ready":True,"assets":{}}
    for key,rel in REQUIRED_ASSETS.items():
        p=root/rel
        ok=p.exists() and p.is_file()
        report["assets"][key]={"path":rel,"present":ok,"sha256":sha256(p) if ok else None}
        report["ready"] &= ok
    return report
