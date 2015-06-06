# Given a triangle, find the minimum path sum from top to bottom. 
# Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space, 
# where n is the total number of rows in the triangle.


#up to down
def minimumTotal(triangle):
    dp = len(triangle)
    if dp == 1:
        return triangle[0][0]
    if dp == 2:
        return triangle[0][0] + min(triangle[1][0], triangle[1][1])
    for i in range(1, dp):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
            elif j == i:
                triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
            else:
                triangle[i][j] = triangle[i][j] + min(triangle[i - 1][j - 1], triangle[i - 1][j])
    triangle[dp - 1].sort()
    return triangle[dp - 1][0]

print minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print minimumTotal([[-1],[2,3],[1,-1,-3]])



#down to up
def minimumTotalI(triangle):
    for i in reversed(range(len(triangle) - 1)):
        for j in range(i + 1):
            triangle[i][j] = triangle[i][j] + min(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


print minimumTotalI([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print minimumTotalI([[-1],[2,3],[1,-1,-3]])



#space complexity: O(n)
def minimumTotalII(triangle):
    dp, totalmini = len(triangle), []
    for i in range(dp):
        totalmini.append(triangle[dp - 1][i])
    for i in reversed(range(dp - 1)):
        for j in range(i + 1):
            totalmini[j] = triangle[i][j] + min(totalmini[j], totalmini[j + 1])
    return totalmini[0]

print minimumTotalII([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print minimumTotalII([[-1],[2,3],[1,-1,-3]])

