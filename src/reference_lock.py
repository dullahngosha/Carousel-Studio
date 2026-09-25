from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class CharacterLock:
    key:str
    image_path:str
    role:str
    uniform:str="dark navy blue"
    lanyard_required:bool=True

LOCKS={
 "nyanzobe":CharacterLock("nyanzobe","assets/references/nyanzobe.png","Mjue Jirani Yako educator"),
 "mbitiyaza":CharacterLock("mbitiyaza","assets/references/mbitiyaza.png","Mjue Jirani Yako educator"),
}

def resolve(names,root="."):
    out=[]
    for raw in names:
        key=raw.strip().lower()
        if key not in LOCKS: continue
        lock=LOCKS[key]; p=Path(root)/lock.image_path
        if not p.exists(): raise FileNotFoundError(f"Approved reference missing: {lock.image_path}")
        out.append(lock)
    return out
