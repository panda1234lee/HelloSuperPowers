import pytest
from calculator.core import add

def test_add_integers():
    assert add(1, 2) == 3

def test_add_floats():
    assert add(1.1, 2.2) == pytest.approx(3.3)

def test_add_mixed_types():
    assert add(1, 2.5) == 3.5
