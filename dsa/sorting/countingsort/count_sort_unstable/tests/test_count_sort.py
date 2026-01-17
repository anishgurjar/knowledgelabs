import pytest
from count_sort_unstable.count_sort import CountingSort


@pytest.mark.parametrize(
    "nums, expected",[
        ([0,1,-2],[-2,0,1]),
        ([45,46,23,32,7,81,2,3,1,9], [1,2,3,7,9,23,32,45,46,81]),
        ([], []),
        ([0],[0]),
        ([0,0,0],[0,0,0]),
        ([11,0,-1],[-1,0,11])
    ]
)
def test_count_sort_sorts_correctly(nums,expected):
    sorter = CountingSort()
    res = sorter.sort(nums)
    assert res == expected

