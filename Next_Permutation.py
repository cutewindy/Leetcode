# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 - 1,3,2
# 3,2,1 - 1,2,3
# 1,1,5 - 1,5,1


def nextPermutation(nums):
    j = -1
    temp = []
    for i in reversed(range(len(nums))):
        if nums[i] > nums[i - 1]:
            j = i - 1
            break
    if j == -1:
        temp = nums[::-1]
    else:
        for i in reversed(range(len(nums))):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        temp = nums[:j + 1] + nums[:j:-1]
    for i in range(len(temp)):
        nums[i] = temp[i]
    return nums

print nextPermutation([1])
print nextPermutation([1, 4, 2, 3])
print nextPermutation([1, 3, 2])
print nextPermutation([3, 2, 1])





# nums = [0, 1, 2, 3, 4, 5, 6]
# n = nums[::2]
# m = nums[4::-1]
# k = nums[:4:-1]
# l = n + m
# print n, m, l, k

#>>>  [0, 2, 4, 6] [4, 3, 2, 1, 0] [0, 2, 4, 6, 4, 3, 2, 1, 0] [6, 5]








