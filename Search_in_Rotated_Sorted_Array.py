# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

def search(nums, target):
    if len(nums) == 0:
        return 
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[j]:
            if nums[mid] < target and target <= nums[j]:
                i = mid + 1
            else:
                j = mid - 1
        else:
            if nums[i] <= target and target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
    return -1

print search([6, 7, 1, 2, 3, 4, 5], 1)
print search([3, 1], 1)
print search([3, 5, 1], 3)