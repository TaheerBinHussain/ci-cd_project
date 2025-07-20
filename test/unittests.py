from project import add, mul, sub, div

def test_add():
    assert add(2, 3) == 5

def test_mul():
    assert mul(2, 3) == 6

def test_sub():
    assert sub(5, 2) == 3

def test_div():
    assert div(10, 2) == 5
