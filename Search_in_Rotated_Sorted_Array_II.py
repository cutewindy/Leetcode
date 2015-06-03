# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?

# Would this affect the run-time complexity? How and why?

# Write a function to determine if a given target is in the array.

def search(nums, target):
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) / 2
        if nums[mid] == target:
            return True
        elif nums[mid] < nums[j]:
            if nums[mid] < target and target <= nums[j]:
                i = mid + 1
            else:
                j = mid - 1
        elif nums[mid] > nums[j]:
            if nums[i] <= target and target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        else:
            j -= 1
    return False

print search([2, 3, 3, 4, 5, 6, 7, 1, 2, 2], 2)
print search([1, 1, 2, 3, 1, 1, 1], 2)
print search([3, 1, 1], 3)
print search([1, 1, 3, 1], 3)
