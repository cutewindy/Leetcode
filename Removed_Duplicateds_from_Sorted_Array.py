# Given a sorted array, remove the duplicates in place such that each element appear only 
# once and return the new length.

# Do not allocate extra space for another array, you must do this in place with constant memory.

# For example,
# Given input array nums = [1,1,2],

# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
# It doesn't matter what you leave beyond the new length.


def removeDuplicates(nums):
    leng = len(nums)
    if leng == 1:
        return leng
    i = 1
    while i < leng:
        if nums[i-1] == nums[i]:
            nums.pop(i)
            leng -= 1
        else:
            i += 1

    return leng, nums

print removeDuplicates([1, 1])
print removeDuplicates([1, 1, 2])
print removeDuplicates([1, 1, 2, 3, 3, 3, 6, 6])


def removeDuplicatesI(nums):
    if len(nums) < 2:
        return len(nums)
    newlen = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[newlen] = nums[i]
            newlen += 1
    return newlen, nums
print removeDuplicatesI([1, 1])
print removeDuplicatesI([1, 1, 2])
print removeDuplicatesI([1, 1, 2, 3, 3, 3, 6, 6])
