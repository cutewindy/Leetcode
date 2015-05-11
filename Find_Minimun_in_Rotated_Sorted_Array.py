# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.

def findMin(nums):
    minnum = nums[0]
    for num in nums:
        minnum = min(num, minnum)
    return minnum

print findMin([0, 1, 2, 4, 5, 6, 7])
        