from app import addition


def test_addition_positive():
    assert addition(2, 3) == 5


def test_addition_negative():
    assert addition(-1, -2) == -3


def test_addition_zero():
    assert addition(0, 0) == 0
    assert addition(5, 0) == 5
    assert addition(0, 5) == 5


def test_addition_float():
    assert addition(2.5, 0.5) == 3.0