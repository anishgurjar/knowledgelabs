print("Simple loop")
arr = [10, 20, 30, 40, 50]

for i in range(len(arr)):
    print(i, arr[i])

print("Reverse Loop")
nums = [10, 20, 30, 40, 50]
i, j = 0, len(nums) - 1 #just set the pointers. 
while i < j: #if they are not allowed to touch, i < j, if they are allowed, i <= j
    nums[i], nums[j] = nums[j], nums[i]
    i+=1
    j-=1
print(nums)