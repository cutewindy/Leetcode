# Given an unsorted array of integers, find the length of the longest consecutive 
# elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.

def longestConsecutive(nums):
    lookup, longest = {num: False for num in nums}, 0
    # print lookup
    for num in nums:
        if lookup[num] == False:
            lookup[num] = True
            i, j, current = num + 1, num - 1, 1
            while i in lookup and lookup[i] == False:
                lookup[i] = True
                current += 1
                i += 1
            while j in lookup and lookup[j] == False:
                lookup[j] = True
                current += 1
                j -= 1
            longest = max(longest, current)
    return longest


print longestConsecutive([100, 4, 200, 1, 3, 2])