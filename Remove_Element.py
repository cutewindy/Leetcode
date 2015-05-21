# Given an array and a value, remove all instances of that value in place and return the new length.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.


def removeElement(nums, val):
    leng = 0
    for num in nums:
        if num != val:
            nums[leng] = num 
            leng += 1
    return leng

print removeElement([1,2,3,4,3,3,2,2,5], 3)