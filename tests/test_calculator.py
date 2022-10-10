import pytest

import calculator

# @pytest.mark.skip(reason="skip reason")
@pytest.mark.parametrize("x, y, result", [
    (7, 3, 10),
    (-3, 5, 2),
    ("Hello", "World", "HelloWorld")
])
def test_add(x, y, result):
    assert calculator.add(x, y) == result

def test_product():
    assert calculator.product(3, 4) == 12
    assert calculator.product(3) == 6
