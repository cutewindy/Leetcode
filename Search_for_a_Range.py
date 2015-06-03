# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

def searchRange(nums, target):
    rang = [-1, -1]
    flag = 1
    for i in range(len(nums)):
        if nums[i] == target and flag == 1:
            rang[0], rang[1] = i, i
            flag = 2
            continue
        if nums[i] == target and flag == 2:
            if i == len(nums) - 1:
                rang[1] = i
            elif nums[i + 1] != target:
                rang[1] = i
                break
    return rang

print searchRange([5, 7, 7, 8, 8, 10], 8)
print searchRange([1], 1)
print searchRange([2, 2], 2)



def searchRangeI(nums, target):
    rang = [-1, -1]
    # i, j = 0, 0
    for i in range(len(nums)):
        if nums[i] == target:
            rang[0] = i
            break
    for j in reversed(range(i, len(nums))):
        if nums[j] == target:
            rang[1] = j
            break
    return rang

print searchRangeI([5, 7, 7, 8, 8, 10], 8)
print searchRangeI([1], 1)
print searchRangeI([2, 2], 2)








