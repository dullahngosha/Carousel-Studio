import pytest
from src.prompt_guard import guard_scene_prompt, sanitize_scene_prompt

@pytest.mark.parametrize("bad",["collage of scenes","2x2 grid","multi-panel poster","split screen"])
def test_blocks_multi_image_language(bad):
    with pytest.raises(ValueError): guard_scene_prompt(bad)

def test_scene_prompt_removes_brand_requests():
    out=sanitize_scene_prompt("Officer scene with immigration logo and footer typography")
    assert "immigration logo" not in out.lower()
    assert "footer typography" not in out.lower()
    assert "one complete standalone" in out.lower()
