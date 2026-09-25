from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import hashlib

@dataclass(frozen=True)
class Asset:
    key: str
    path: Path
    sha256: str

def digest(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def require_asset(key: str, path: str|Path) -> Asset:
    p=Path(path)
    if not p.is_file(): raise FileNotFoundError(f"Required approved asset missing: {key} -> {p}")
    return Asset(key,p,digest(p))

def production_assets(root="assets"):
    r=Path(root)
    return {
      "logo": require_asset("official_immigration_logo",r/"official/immigration-logo.png"),
      "nyanzobe": require_asset("nyanzobe",r/"references/nyanzobe.png"),
      "mbitiyaza": require_asset("mbitiyaza",r/"references/mbitiyaza.png"),
    }
