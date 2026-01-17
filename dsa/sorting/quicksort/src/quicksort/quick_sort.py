from typing import List

class QuickSort:

    def __init__(self):
        pass

    def _partition(self, nums, low, high):
        pivot = high
        i = low
        for j in range(low, high):
            if(nums[j] <= nums[pivot]):
                nums[i],nums[j] = nums[j], nums[i]
                i+=1
        nums[pivot], nums[i] = nums[i], nums[pivot]
        return i


    def _quicksort(self, nums, low, high):
        if(low >= high):
            return
        pivot = self._partition(nums, low, high)
        self._quicksort(nums, low, pivot - 1)
        self._quicksort(nums, pivot + 1, high)

    def sort(self, nums):
        low, high = 0, len(nums) - 1
        self._quicksort(nums, low, high)
        return nums