from calculator import add, divide
import pytest

def test_add():

    assert add(1, 2) == 3
    assert add(-1,1) == 0
    assert add (0,0) == 0

def test_divide():
    assert divide(1,1) == 1
    assert divide(0,-1) == 0
    with pytest.raises(ValueError, match="Cannot divide by 0"):
        divide(10,0)
