from typing import List

def main(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r: 
        
        mid = (l+r)//2

        if nums[mid] == target:
            return mid
        
        if l == r:
            return -1

        elif nums[mid] < nums[r]:

            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        elif nums[mid] > nums[r]:
            if target >= nums[l] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

    return -1

if __name__ == "__main__":
    print(main([1,3], 0))