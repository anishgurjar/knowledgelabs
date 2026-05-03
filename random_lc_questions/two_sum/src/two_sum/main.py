from os import name
from typing import List


def main(nums: List[int], target: int):

    n = len(nums)
    hashmap = {}
    for i in range(n):
        if target - nums[i] in hashmap:
            return [hashmap[target - nums[i]],i]
        hashmap[nums[i]] = i

if name == "__main__":
    main()