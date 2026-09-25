import json
from pathlib import Path
try:
    from .batch_plan import split_batches, output_path
    from .validate_plan import validate_slide_plan
    from .qc import assert_unique_files
except ImportError:
    from batch_plan import split_batches, output_path
    from validate_plan import validate_slide_plan
    from qc import assert_unique_files

def build_jobs(plan_path, output_root="outputs"):
    slides=json.loads(Path(plan_path).read_text(encoding="utf-8"))
    validate_slide_plan(slides); batches=split_batches(slides); jobs=[]
    for batch_index,batch in enumerate(batches,1):
        for slide in batch:
            sid=int(slide["id"])
            jobs.append({"slide_id":sid,"batch":batch_index,"prompt":slide["image_prompt"],"negative_prompt":slide.get("negative_prompt",""),"output":str(output_path(output_root,sid))})
    assert_unique_files([j["output"] for j in jobs]); return jobs
if __name__=="__main__":
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument("plan"); ap.add_argument("--output-root",default="outputs")
    a=ap.parse_args(); print(json.dumps(build_jobs(a.plan,a.output_root),indent=2,ensure_ascii=False))
