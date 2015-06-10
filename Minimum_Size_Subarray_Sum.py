# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a subarray of which the sum >= s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

# click to show more practice.

# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

def minSubArrayLen(s,  nums):
    i, j, amount, ministep = 0, 0, 0, 999
    while i <= j and j < len(nums) and amount < s:
        amount += nums[j]
        while i <= j and amount >= s:
            ministep = min(ministep, j - i + 1)
            amount -= nums[i]
            i += 1
        j += 1
    if ministep == 999:
        return 0
    return ministep


print minSubArrayLen(7, [2, 3, 1, 2, 4, 3])    


def minSubArrayLenI(s, nums):
    first = True
    i, j, amount, curstep, ministep = 0, 0, 0, 0, 0
    nums = nums + [0]
    while i <= j and j < len(nums):
        if amount < s:
            amount += nums[j]
            curstep += 1
            j += 1
        else:
            if first:
                ministep = curstep
                first = False
            else:
                ministep = min(ministep, curstep)
            if i < j:
                amount -= nums[i]
                curstep -= 1
                i += 1
    return ministep

print minSubArrayLenI(7, [2, 3, 1, 2, 4, 3]) 










