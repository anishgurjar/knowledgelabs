from longest_consecutive_sequence.main import main
import pytest

@pytest.mark.parametrize("input,expected", [
    ([1,100,2,200,201,3,202,4,5],5),
    ([1,100,2,200,201,202,4,203,199], 5),
    ([1], 1),
    ([], 0),
    ([-1,-2,-3], 3),
    ([-1,-2,-3, -9,-8,-7,-6,-5], 5)
])
def test_main(input, expected):
    assert main(input) == expected