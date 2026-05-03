
from collections import defaultdict


def main(s: str, k: int) -> int:

    """
    AABABBA
    """

    l = 0
    result_length = 0
    substring_map = defaultdict(int)

    for r in range(len(s)):

        substring_map[s[r]]+=1

        while (r-l+1) - max(substring_map.values()) > k: 
            substring_map[s[l]]-=1
            l+=1
        
        curr_length = r - l + 1
        result_length = max(result_length, curr_length)

    return result_length


if __name__ == "__main__":
    print(main('AABABBA', 1))