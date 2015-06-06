# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

# Note: m and n will be at most 100.

def uniquePathWithObstacles(obstacleGrid):
    m, n =len(obstacleGrid), len(obstacleGrid[0])
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            for k in range(i, m):
                obstacleGrid[k][0] = 1
    for j in range(n):
        if obstacleGrid[0][j] == 1:
            for k in range(j, n):
                obstacleGrid[0][k] = 1

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = 1
            else:
                obstacleGrid[i][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:                
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
    return obstacleGrid[m - 1][n - 1]

print uniquePathWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print uniquePathWithObstacles([[1, 0, 0], [0, 0, 0]])
print uniquePathWithObstacles([[1]])
print uniquePathWithObstacles([[0, 0], [1, 1], [0, 0]])



def uniquePathWithObstaclesI(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    ways = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 0:
                if i == 0 and j == 0:
                    ways[i][j] = 1
                elif i == 0:
                    ways[i][j] = ways[i][j - 1]
                elif j == 0:
                    ways[i][j] = ways[i - 1][j]
                else:
                    ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
    return ways[m - 1][n - 1]

print uniquePathWithObstaclesI([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print uniquePathWithObstaclesI([[1, 0, 0], [0, 0, 0]])
print uniquePathWithObstaclesI([[1]])
print uniquePathWithObstaclesI([[0, 0], [1, 1], [0, 0]])





