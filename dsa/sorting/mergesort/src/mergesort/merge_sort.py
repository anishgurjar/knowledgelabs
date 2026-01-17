class MergeSort:

    def __init__(self):
        pass

    def sort(self,nums):
        low, high = 0, len(nums) - 1
        self._merge_sort(nums,low,high)
        return nums

    def _merge_sort(self, nums, low, high):
        
        if(low>=high):
            return
        mid = low + (high-low)//2
        self._merge_sort(nums,low,mid)
        self._merge_sort(nums,mid+1, high)
        
        self._merge(nums,low,mid,high)
    
    def _merge(self, nums, low, mid, high):
        
        res = []
        i, j = low, mid+1
        while i <= mid and j <= high:
            if(nums[i] < nums[j]):
                res.append(nums[i])
                i+=1
            else:
                res.append(nums[j])
                j+=1
        #backfill
        while(i <= mid):
            res.append(nums[i])
            i+=1

        while(j <= high):
            res.append(nums[j])
            j+=1

        k = low
        for i in res:
            nums[k] = i
            k+=1
        
        