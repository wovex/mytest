from main import add


def test_add():
    assert add(1,3) == 4

def test_add1():
    assert add(1,5) == 6


def test_add2():
    assert add(1,7) == 8
