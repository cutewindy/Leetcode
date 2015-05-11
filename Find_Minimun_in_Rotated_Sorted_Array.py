# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.

def findMin(nums):
    minnum = min(nums)
    return minnum

print findMin([0, 1, 2, 4, 5, 6, 7])


def findMinI(nums):
    star, end = 0, len(nums) - 1
    min = nums[0]
    while star <= end:
        mid = (star + end) / 2
        if nums[mid] >= min:
            star = mid + 1
        else:
            min = nums[mid]
            end = mid

    return min

print findMinI([0, 1, 2, 4, 5, 6, 7]) 
print findMinI([4, 5, 6, 7, 0, 1, 2])   
print findMinI([1])
print findMinI([2, 1]) 



def findMinII(nums):
    if nums[0] <= nums[-1]:
        return nums[0]
    mid = len(nums) / 2
    if nums[mid] < nums[mid-1]:
        return nums[mid]
    if nums[mid] > nums[-1]:
        return findMinII(nums[mid+1:])
    else:
        return findMinII(nums[:mid])
    
        
print findMinII([0, 1, 2, 4, 5, 6, 7]) 
print findMinII([4, 5, 6, 7, 0, 1, 2])   
print findMinII([1])
print findMinII([2, 1]) 
print findMinII([1, 2])
    
    
    
    
    

  