def searchInsert(nums, target):
#     count = 0
    for num in nums:
        if num >= target:
            return nums.index(num)
        
    return len(nums)
#         else:
#             count += 1
#     if count == len(nums):
#         return len(nums)




print searchInsert([1, 3, 5, 6], 5)
print searchInsert([1, 3, 5, 6], 2)
print searchInsert([1], 2)