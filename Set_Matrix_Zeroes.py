# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# click to show follow up.

# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for row in rows:
        for j in range(n):
            matrix[row][j] = 0
    for col in cols:
        for i in range(m):
            matrix[i][col] = 0
    return matrix

print setZeroes([[1,2,3],[2,0,3],[0,1,2]])
print setZeroes([[1, 2, 3, 0], [4, 0, 2, 1], [1, 3, 2, 0]])
print setZeroes([[0]])
print setZeroes([[3,5,5,6,9,1,4,5,0,5],[2,7,9,5,9,5,4,9,6,8],[6,0,7,8,1,0,1,6,8,1],[7,2,6,5,8,5,6,5,0,6],[2,3,3,1,0,4,6,5,3,5],[5,9,7,3,8,8,5,1,4,3],[2,4,7,9,9,8,4,7,3,7],[3,5,2,8,8,2,2,4,9,8]])


def setZeroesI(matrix):
    m, n = len(matrix), len(matrix[0])
    row_0, col_0 = 0, 0
    # Find whether the first row or col have 0
    for i in range(m):
        if matrix[i][0] == 0:
            row_0 = 1
            break
    for j in range(n):
        if matrix[0][j] == 0:
            col_0 = 1
            break
    # set the first row and col of the location of 0 to 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0], matrix[0][j] = 0, 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if row_0 == 1:
        for i in range(m):
            matrix[i][0] = 0
    if col_0 == 1:
        for j in range(n):
            matrix[0][j] = 0
    return matrix

print setZeroesI([[1,2,3],[2,0,3],[0,1,2]])
print setZeroesI([[1, 2, 3, 0], [4, 0, 2, 1], [1, 3, 2, 0]])
print setZeroesI([[0]])
print setZeroesI([[3,5,5,6,9,1,4,5,0,5],[2,7,9,5,9,5,4,9,6,8],[6,0,7,8,1,0,1,6,8,1],[7,2,6,5,8,5,6,5,0,6],[2,3,3,1,0,4,6,5,3,5],[5,9,7,3,8,8,5,1,4,3],[2,4,7,9,9,8,4,7,3,7],[3,5,2,8,8,2,2,4,9,8]])


