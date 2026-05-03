from unittest import expectedFailure
from top_k_freq_elements.main import main
import pytest


@pytest.mark.parametrize("a,b,expected",[
    ([1,1,1,2,2,3], 2, [[1,2]]),
    ([1,1,1,2,2,2], 2, [[1,2]]),
    ([1,1,1,2,2,2], 1, [[1], [2]]),
    ([], 2, [[]]),
])
def test_main(a,b,expected):
    assert main(a,b) in expected