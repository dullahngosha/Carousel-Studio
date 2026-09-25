from __future__ import annotations
import time, uuid
from pathlib import Path
import json, requests

class ComfyClient:
    def __init__(self, base_url="http://127.0.0.1:8188", timeout=120):
        self.base_url=base_url.rstrip("/")
        self.timeout=timeout
        self.client_id=str(uuid.uuid4())
    def queue(self, workflow):
        r=requests.post(self.base_url+"/prompt",json={"prompt":workflow,"client_id":self.client_id},timeout=30)
        r.raise_for_status()
        return r.json()["prompt_id"]
    def history(self, prompt_id):
        r=requests.get(self.base_url+"/history/"+prompt_id,timeout=30); r.raise_for_status(); return r.json()
    def wait(self,prompt_id,poll=1.0):
        deadline=time.time()+self.timeout
        while time.time()<deadline:
            data=self.history(prompt_id)
            if prompt_id in data: return data[prompt_id]
            time.sleep(poll)
        raise TimeoutError("ComfyUI job timed out: "+prompt_id)
    @staticmethod
    def load_workflow(path):
        return json.loads(Path(path).read_text(encoding="utf-8"))
