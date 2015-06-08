# Given an array S of n integers, are there elements a, b, c 
 # in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},

#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

def threeSum(nums):
    nums.sort()
    i, zeroArray = 0, []
    while i < len(nums) - 2:
        j, k = i + 1, len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                zeroArray.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1
        i += 1
        while i < len(nums) - 2 and nums[i] == nums[i - 1]:
            i += 1
    return zeroArray


print threeSum([0, -6, -5, -4, -1, 4, 5, 6])
print threeSum([-1, 0, 1, 2, -1, -4])
print threeSum([0, 0, 0 ,0])


