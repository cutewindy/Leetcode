# Given an array of integers and an integer k, find out whether there there are 
# two distinct indices i and j in the array such that nums[i] = nums[j] and the 
# difference between i and j is at most k.


def containsNearbyDuplicate(nums, k):
    dictnum = {}
    for i in range(len(nums)):
        j = dictnum.get(nums[i])
        if j >= 0 and i - j <= k:
            return True
        dictnum[nums[i]] = i
    return False 



print containsNearbyDuplicate([1, 2, 2, 3, 1, 4, 6, 7, 9], 2)
print containsNearbyDuplicate([1], 1)
print containsNearbyDuplicate([1, 2, 1], 0)