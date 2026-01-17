import pytest 
from quicksort.quick_sort import QuickSort

@pytest.mark.parametrize(
    "nums, expected", [
        ([45,46,23,32,7,81,2,3,1,9], [1,2,3,7,9,23,32,45,46,81]),
        ([], []),
        ([0],[0]),
        ([0,0,0],[0,0,0]),
        ([11,0,-1],[-1,0,11])
    ]
)
def test_quicksort_sorts_correctly(nums, expected):
    sorter = QuickSort()
    assert sorter.sort(nums) == expected