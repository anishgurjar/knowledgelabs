from typing import Any, List
from collections import defaultdict

def main(strs: List[str]) -> List[List[str]]:

    my_map = defaultdict[str, list](list)

    for i in strs: 
        key = "".join(sorted(i))
        my_map[key].append(i)
    
    return list(my_map.values())

if __name__ == "__main__":
    print(main(["eat","tea","tan","ate","nat","bat"]))