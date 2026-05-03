from group_anagrams.main import main

import pytest


@pytest.mark.parametrize("input,output", [
    (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
    (["", "eat"], [[""],["eat"]]),
    ([""], [[""]]),
    ([],[[]])
])
def test_main():
    pass