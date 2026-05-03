from typing import List
from collections import defaultdict

def main(nums: List[int], k: int) -> List[int]:

    """
    {1: 3, 2: 2, 3: 1}
    """

    countermap = defaultdict(int)
    
    for i in nums:
        countermap[i] += 1
    
    bucket = list(countermap.items())    
    bucket = sorted(bucket, key = lambda x:x[1], reverse=True)

    counter=k
    res = []

    for i in bucket:
        if counter == 0:
            return res    
        res.append(i[0])
        counter -= 1

    return res

if __name__ == "__main__":
    main()
