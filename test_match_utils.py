import math_utils


def test_add() -> None:
    assert math_utils.add(0, 1) == 1
    assert math_utils.add(2, 3) == 5
    assert math_utils.add(-10, 5) == -5

def test_multiply() -> None:
    assert math_utils.multiply(0, 1) == 0
    assert math_utils.multiply(2, 3) == 6
    assert math_utils.multiply(-10, 5) == -50
