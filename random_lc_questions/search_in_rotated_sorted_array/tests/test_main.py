from search_in_rotated_sorted_array.main import main
import pytest

@pytest.mark.parametrize('nums,target,expected', [
    ([4,5,6,7,0,1,2], 0, 4),
    ([0,1,2], 3, -1),
    ([1], 0, -1),
    ([1], 1, 0),
    ([1, 2], 1, 0),
    ([1, 2], 2, 1),
    ([2, 1], 1, 1),
    ([2, 1], 2, 0)
])
def test_main(nums, target, expected):
    assert main(nums, target) == expected