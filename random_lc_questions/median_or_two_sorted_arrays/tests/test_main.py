from median_or_two_sorted_arrays.main import main 
import pytest


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([1,3],[2],2),
    ([1,2],[3,4], 2.5),
    ([1,2],[],1.5),
    ([],[2,3], 2.5),
    ([1],[2,3],2),
    ([],[], 0)
])
def test_main():
    pass