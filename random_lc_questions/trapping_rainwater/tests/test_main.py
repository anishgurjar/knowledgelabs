from trapping_rainwater.main import main
import pytest

@pytest.mark.parametrize("input,expected",[
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([0,1,0],0),
    ([1,0,0],0),
    ([0,0,1],0),
    ([1,0,1],1),
    ([2,0,1],1),
    ([1], 0)
])
def test_main(input, expected):
    assert main(input) == expected