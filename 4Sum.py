# Given an array S of n integers, are there elements a, b, c, 
# and d in S such that a + b + c + d = target? Find all unique quadruplets 
# in the array which gives the sum of target.

# Note:
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
# The solution set must not contain duplicate quadruplets.
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)


def fourSum(nums, target):
    nums.sort()
    foursum = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            target2 = target - nums[i] - nums[j]
            k, l = j + 1, len(nums) - 1
            while k < l:
                if nums[k] + nums[l] == target2:
                    foursum.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif nums[k] + nums[l] < target2:
                    k += 1
                else:
                    l -= 1
    return foursum

print fourSum([0, 0, 0, 0], 0)
print fourSum([1, 0, -1, 0, -2, 2], 0)



def fourSumI(nums, target):
    nums.sort()
    foursum, lookup = set(), {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] in lookup:
                lookup[nums[i] + nums[j]].append((i, j))
            else:
                lookup[nums[i] + nums[j]] = [(i, j)]

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            if target - nums[i] - nums[j] in lookup:
                for k in lookup[target - nums[i] - nums[j]]:
                    if k[0] > j:
                        foursum.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))

    return [list(i) for i in foursum]


print fourSumI([0, 0, 0, 0], 0)
print fourSumI([1, 0, -1, 0, -2, 2], 0)


