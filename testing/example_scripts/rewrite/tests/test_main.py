from testing.example_scripts.rewrite.src.main import func

def test_func(a: int, b: int):
    assert func(a, b)>0