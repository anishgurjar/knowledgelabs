from find_min_in_rotated_sorted_array.main import main
import pytest


@pytest.mark.parametrize('input, expected',[
    ([4,5,6,7,0,1,2], 0),
    ([11,13,15,17], 11),
    ([1,2,3], 1),
    ([1], 1),
    ([-1,1], -1),
    ([3,4,0,1,2],0),
    ([3,5,6], 3)
])
def test_main(input, expected):
    assert main(input) == expected