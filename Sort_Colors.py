# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# 
# Note:
# You are not suppose to use the library's sort function for this problem.


def sortColorsI(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j+1] < nums[j]:
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp
    return nums 

print sortColorsI([0, 0, 2, 2, 2, 1, 2, 0, 2, 2, 1, 1, 1, 0])
    
def sortColorsII(nums):
    