# Given an array of integers, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice in the array,
#  and it should return false if every element is distinct.

def containsDupliate(nums):
    dictnum = {}
    for i in range(len(nums)):
        if dictnum.get(nums[i]) != None:
            return True
        else:
            dictnum[nums[i]] = i
    return False

print containsDupliate([1, 2, 3, 4, 2, 5])
print containsDupliate([1, 2 ,3 ,4 ,5 ,6])


def containsDupliateI(nums):
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

print containsDupliateI([1, 2, 3, 4, 2, 5])
print containsDupliateI([1, 2 ,3 ,4 ,5 ,6])