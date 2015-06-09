# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space.

def firstMissingPositive(nums):
    lookup = {}
    for i in range(len(nums)):
        lookup[nums[i]] = i

    for i in range(1, 99999):
        if i in lookup:
            continue
        else:
            return i


print firstMissingPositive([1, 2, 0])
print firstMissingPositive([3, 4, -1, 1])
print firstMissingPositive([2])



def firstMissingPositiveI(nums):
    i = 0
    while i < len(nums):
        if nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i + 1
    return len(nums) + 1

print firstMissingPositiveI([1, 2, 0])
print firstMissingPositiveI([3, 4, -1, 1])
print firstMissingPositiveI([2])



