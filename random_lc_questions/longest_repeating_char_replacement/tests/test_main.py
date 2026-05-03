from longest_repeating_char_replacement.main import main
import pytest

@pytest.mark.parametrize("s,k,expected",[
    ('ABAB', 2, 4),
    ('AABABBA', 1, 4),
    ('ABCAAB', 2, 5),
    ('', 2, 0),
    ('A', 1, 1),
    ('AA', 2, 2),
    ('AB', 2, 2),
    ('ABBB', 2, 4)
])
def test_main(s,k,expected):
    assert main(s,k) == expected