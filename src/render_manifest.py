import json, datetime
from pathlib import Path
def write_manifest(project_name,jobs,assets,out="outputs/manifest.json"):
    data={"project":project_name,"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"policy":"ONE SLIDE = ONE IMAGE FILE","jobs":jobs,"assets":{k:{"path":str(v.path),"sha256":v.sha256} for k,v in assets.items()}}
    p=Path(out); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding="utf-8"); return p
