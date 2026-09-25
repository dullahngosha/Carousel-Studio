from pathlib import Path
from PIL import Image
EXPECTED=(1080,1350)
class QCError(RuntimeError): pass
def inspect_image(path):
    p=Path(path)
    if not p.exists(): raise QCError("Missing output: "+str(p))
    with Image.open(p) as im: size=im.size; fmt=im.format
    if size != EXPECTED: raise QCError(f"Wrong size {size}; expected {EXPECTED}")
    return {"path":str(p),"size":size,"format":fmt,"passed":True}
def assert_unique_files(paths):
    resolved=[str(Path(p).resolve()) for p in paths]
    if len(resolved)!=len(set(resolved)): raise QCError("Multiple slides target the same output file.")
