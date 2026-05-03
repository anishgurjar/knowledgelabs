from typing import List

def main(nums1: List[int], nums2: List[int]) -> int: 


    l, r = 0, len(nums2) - 1
    half_count = (len(nums1) + len(nums2))//2

    while l <= r :

        mid = (l+r)//2

        nums_1_left_partition_index = half_count - mid + 1
         
        if nums1[nums_1_left_partition_index] <= nums2[mid + 1] and nums2[mid] <= nums1[nums_1_left_partition_index + 1]:
            return the median
        
        elif
