# Given n non-negative integers a1, a2, ..., an, where each represents a 
# point at coordinate (i, ai). n vertical lines are drawn such that the two 
# endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together 
# with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container.


def maxArea(height):
    if len(height) < 2:
        return 
    i, maxArea, j = 0, 0, len(height) - 1
    while i < j:
        maxArea = max(min(height[i], height[j]) * (j - i), maxArea)
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return maxArea

print maxArea([1, 3, 5, 2, 6, 8, 2, 5, 2])
