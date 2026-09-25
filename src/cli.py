from __future__ import annotations
import argparse, json
from .pipeline import build_jobs
from .preflight import check
from .layout import spec

def main():
    ap=argparse.ArgumentParser(prog="carousel-studio")
    sub=ap.add_subparsers(dest="cmd",required=True)
    p=sub.add_parser("preflight"); p.add_argument("--root",default=".")
    p=sub.add_parser("jobs"); p.add_argument("plan"); p.add_argument("--output-root",default="outputs")
    sub.add_parser("layout")
    a=ap.parse_args()
    if a.cmd=="preflight": data=check(a.root)
    elif a.cmd=="jobs": data=build_jobs(a.plan,a.output_root)
    else: data=spec()
    print(json.dumps(data,indent=2,ensure_ascii=False))
if __name__=="__main__": main()
