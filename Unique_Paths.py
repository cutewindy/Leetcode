# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?


def uniquePaths(m, n):
    cnt = [[1] for i in range(m)]
    for i in range(1, n):
        cnt[0].append(1)
    for i in range(1, m):
        for j in range(1, n):
            cnt[i].append(cnt[i][j-1] + cnt[i-1][j])
    return cnt, cnt[m-1][n-1]
    


print uniquePaths(2, 2)
print uniquePaths(3, 3)
print uniquePaths(4, 5)
print uniquePaths(5, 4)

