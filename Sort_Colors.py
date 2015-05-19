# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# 
# Note:
# You are not suppose to use the library's sort function for this problem.

#bubble sort
#time complexity: O(n**2)
#space complexity:O()
def sortColorsI(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j+1] < nums[j]:
#                 temp = nums[j+1]
#                 nums[j+1] = nums[j]
#                 nums[j] = temp
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums 

print sortColorsI([0, 0, 2, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 0])


#straight insertion sort
#time complexity: O(n**2)
#space complexity: 
def sortColorsII(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            j = i - 1
            temp = nums[i]
            while j >= 0 and nums[j] > temp:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = temp
    return nums

print sortColorsII([0, 0, 2, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 0]) 


#shell's sort
#time complexity:
#space complexity:
def sortColorsIII(nums):
    d = len(nums) / 2
    while d > 0:
        for i in range(d):
            for j in range(i+d, len(nums)):
                if nums[j] < nums[j-d]:
                    temp = nums[j]
                    k = j-d
                    while k >=0 and nums[k] > temp:
                        nums[k+d] = nums[k]
                        k -= d
                    nums[k+d] = temp
        d = d / 2
    return nums

print sortColorsIII([0, 0, 2, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 0])       


#simple selection sort:
#time complexity:
#space complexity:
def sortColorsIV(nums):
    for i in range(len(nums)-1):
            temp = nums[i]
            for j in range(i+1, len(nums)):
                if temp > nums[j]:
                    nums[j], temp = temp, nums[j]
            nums[i] = temp
    return nums
    
print sortColorsIV([0, 0, 2, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 0])


#
def sortColorsV(nums):






























    

        