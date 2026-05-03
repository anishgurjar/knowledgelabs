from valid_anagram.main import main
import pytest


@pytest.mark.parametrize("a,b,expected",[
    ("racecar","racecar",True),
    ("anish", "qerewer", False),
    ("", "", True),
    ("a n i n a", "anina", False),
    ("anina", "innaa", True)
])
def test_main(a,b,expected):
    
    assert main(a, b) == expected