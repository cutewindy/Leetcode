# A peak element is an element that is greater than its neighbors.

# Given an input array where num[i] != num[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that num[-1] = num[n] = - no limit.

# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

# click to show spoilers.

# Note:
# Your solution should be in logarithmic complexity.


def findPeakElement(nums):
    if len(nums) == 0:
        return 
    if len(nums) == 1 or nums[0] > nums[1]:
        return 0
    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return len(nums) - 1
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
            return i

print findPeakElement([1, 2, 3, 1])

def findPeakElementI(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if right - left == 1:
            if nums[left] > nums[right]:
                return left
            return right
        mid = (left + right) / 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid
    return left
print findPeakElementI([1, 2, 3, 1]) 









