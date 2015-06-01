# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold 
# additional elements from nums2. The number of elements initialized in nums1 and nums2 are m 
# and n respectively.

def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1

print merge([0, 1, 2, 3, 4, 5, 0, 0, 0], 6, [3, 5, 7], 3)
print merge([4, 5, 6, 0, 0, 0, 0], 3, [2, 3, 4, 7], 4)
print merge([0], 0, [1], 1)


