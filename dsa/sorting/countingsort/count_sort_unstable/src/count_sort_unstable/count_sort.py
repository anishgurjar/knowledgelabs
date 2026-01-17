class CountingSort:

    def __init__(self):
        pass

    def sort(self, nums):
        if(len(nums)==0):
            return nums
        min_val = min(nums)
        max_val = max(nums)
        return self._countingsort(nums,min_val,max_val)

    def _countingsort(self, nums, min_val, max_val):

        length = max_val - min_val
        offset = -min_val
        counts = [0] * (length+1)

        for num in nums:
            counts[num + offset] += 1
            print(counts)
         
        index_to_put_at = len(nums)-1
        for i in range(len(counts)-1, -1, -1):
            while(counts[i] > 0):
                nums[index_to_put_at] = i-offset
                index_to_put_at -= 1
                counts[i]-=1

        return nums
