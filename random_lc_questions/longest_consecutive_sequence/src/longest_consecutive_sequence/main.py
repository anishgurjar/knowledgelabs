from typing import List

def main(nums: List[int]) -> List[int]:
    """

    [1,100,2,200,201,202,4,203,199]
    
    """

    range_length = 0

    nums_set = set(nums)
    for i in nums:
        
        if i not in nums_set:
            continue

        prev_val = i - 1
        while prev_val in nums_set:
            nums_set.remove(prev_val)
            prev_val = prev_val - 1
        
        next_val = i + 1
        while next_val in nums_set:
            nums_set.remove(next_val)
            next_val = next_val + 1
        
        nums_set.remove(i)

        if (next_val - prev_val) > range_length: 
            range_length = next_val - prev_val - 1
        

    return range_length


if __name__ == "__main__":

    print(main([1,100,2,200,201,202,4,203,199]))