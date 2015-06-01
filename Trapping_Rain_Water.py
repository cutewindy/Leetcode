# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.

# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


def trap(height):
    left, right, secH, water = 0, len(height) - 1, 0, 0
    print right
    while left < right:
        if height[left] < height[right]:
            secH = max(secH, height[left])
            water += secH - height[left]
            left += 1
        else:
            secH = max(secH, height[right])
            water += secH - height[right]
            right -= 1
    return water

print trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])




