# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,

# Consider the following matrix:

# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return True
    return False

print searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
print searchMatrix([[1, 3]], 3)
print searchMatrix([[1]], 0)

def searchMatrixI(matrix, target):
    row, col = len(matrix) - 1, len(matrix[0]) - 1
    for i in range(row+1):
        if matrix[i][col] == target:
            return True
        if matrix[i][col] > target:
            for j in range(col):
                if matrix[i][j] == target:
                    return True

    return False

print searchMatrixI([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
print searchMatrixI([[1, 3]], 3)
print searchMatrixI([[1]], 0)

def searchMatrixII(matrix, target):
    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] > target:
            j -= 1
        elif matrix[i][j] < target:
            i += 1
        else:
            return True
    return False

print searchMatrixII([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
print searchMatrixII([[1, 3]], 3)
print searchMatrixII([[1]], 0)





