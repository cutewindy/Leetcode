# Given n non-negative integers representing the histogram's bar height 
# where the width of each bar is 1, find the area of largest rectangle in the histogram.


# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# For example,
# Given height = [2,1,5,6,2,3],
# return 10.


# def largestRectangleArea(height):
#     stack = []
#     t = stack.pop()
#     return t

# print largestRectangleArea([2, 1, 5, 6, 2, 3])

def largestRectangleArea(height):
    stack = []
    i, maxarea = 0, 0
    while i <= len(height):
        if (not stack) or (i < len(height) and height[i] > height[stack[-1]]):
            stack.append(i)
            i += 1
        else:
            last = stack.pop()
            if not stack:
                maxarea = max(maxarea, height[last] * i)
            else:
                maxarea = max(maxarea, height[last] * (i - stack[-1] - 1))
    return maxarea

    # increasing, area, i = [], 0, 0
    # while i <= len(height):
    #     if len(increasing) == 0 or (i < len(height) and height[i] > height[increasing[-1]]):
    #         increasing.append(i)
    #         print i, increasing
    #         i += 1
    #     else:
    #         last = increasing.pop()
    #         if len(increasing) == 0:
    #             area = max(area, height[last] * i)
    #         else:
    #             area = max(area, height[last] * (i - increasing[-1] - 1))
    #             print i, last, area
    # return area

print largestRectangleArea([2, 1, 5, 6, 2, 3])