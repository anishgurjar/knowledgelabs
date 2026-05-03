import pytest

from longest_substr_without_repeating_chars.main import main


@pytest.mark.parametrize("input,output", [
    ("abcabcbb", 3),
    ("", 0),
    ("aa", 1),
    ("a", 1),
    (" a", 2),
])
def test_main(input, output):
    assert main(input) == output