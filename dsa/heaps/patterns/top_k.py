"""
Given an array nums, return top 3 largest elements in the array
"""
import heapq
nums = [9, 3, 7, 1, -2, 6, 8]

negated_nums = [-x for x in nums]
heapq.heapify(negated_nums)
res = []
while len(res) != 3:
    res.append(heapq.heappop(negated_nums) * -1)

print(res)

