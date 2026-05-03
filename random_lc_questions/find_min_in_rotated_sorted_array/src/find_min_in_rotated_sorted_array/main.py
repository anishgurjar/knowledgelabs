from typing import List

def main(nums: List[int]) -> int:
    """
        - if nums[mid] >= nums[l] => for sure not the lowest number. lower number is ahead -> l = mid + 1
        - if l == mid -> that's the lowest number. 
        - 
    """

    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r)//2

        if nums[mid] <= nums[r]:
            r = mid
        else:
            l = mid + 1

    return nums[l]


if __name__ == "__main__":
    print(main([11,13,15,17]))