# Given an array S of n integers, find three integers in S such that the sum is 
# closest to a given number, target. Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

    # The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

def threeSumClosest(nums, target):
    first = True
    nums.sort()
    for i in range(len(nums)):
        j, k = i + 1, len(nums) - 1
        while j < k:
            curSum = nums[i] + nums[j] + nums[k]
            if first:
                closeSum = curSum
                first = False
            elif abs(curSum - target) < abs(closeSum - target):
                closeSum = curSum
            if closeSum == target:
                return curSum
            if curSum < target:
                j += 1
            else:
                k -= 1

    return closeSum

print threeSumClosest([-1, 2, 1, -4], -1)
print threeSumClosest([1,2,4,8,16,32,64,128], 82)
