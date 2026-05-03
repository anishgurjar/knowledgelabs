import pytest
from min_window_substr.main import main


@pytest.mark.parametrize("s,t,expected",[
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("ADOBECODEBANC", "PQR", ""),
    ("", "ABC", ""),
    ("", "", "")
])
def test_main(s,t,expected):
    assert main(s,t) == expected