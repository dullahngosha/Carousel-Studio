from src.validate_plan import validate_prompt
from src.batch_plan import split_batches

def test_rejects_collage():
    try:
        validate_prompt("make a collage of four panels")
        assert False
    except ValueError:
        assert True

def test_batches_10_5():
    a,b=split_batches([{"id":i} for i in range(1,16)])
    assert len(a)==10 and len(b)==5
