from two_sum.main import main

import pytest


@pytest.mark.parametrize("a,b,expected", [
    ([1,2,3,4], 4, [0,2])
])
def test_main(a,b,expected):
    
    assert main(a,b) == expected