# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?

# For example,
# Given sorted array nums = [1,1,1,2,2,3],

# Your function should return length = 5, with the first five elements 
# of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.


def removeDuplicates(nums):
    if len(nums) < 3:
        return len(nums)
    i, index, count = 1, 1, 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            count += 1
        else:
            count = 1
        if count < 3:
            nums[index] = nums[i]
            index += 1
        i += 1
    return index


print removeDuplicates([1, 2, 2, 2, 3, 3, 4, 4, 4, 5])
print removeDuplicates([1, 1, 1, 2, 2, 3])
print removeDuplicates([1, 1, 1, 1, 1, 1, 1])