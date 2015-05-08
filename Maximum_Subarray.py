# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

# For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# the contiguous subarray [4, -1, 2, 1] has the largest sum = 6


def maxSubArray(nums):
    cursum, maxsum = 0.0, 0.0
    for num in nums:
        cursum = max(num, num + cursum)
        print cursum
        maxsum = max(cursum, maxsum)
        print maxsum
    return maxsum

print maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
