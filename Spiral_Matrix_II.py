# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

def printMatrix(matrix):
    for row in matrix:
        print "  ".join(str(row))

def generateMatrix(n):
    if n == 0:
        return 
    matrix = [[0]*n for i in range(n)]
    left, right, top, bottom, num = 0, n - 1, 0, n - 1, 1
    while left < right and top < bottom:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        for i in range(top + 1, bottom):
            matrix[i][right] = num
            num += 1
        for i in reversed(range(left, right + 1)):
            matrix[bottom][i] = num
            num += 1
        for i in reversed(range(top + 1, bottom)):
            matrix[i][left] = num
            num += 1
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    if n % 2 == 1:
        matrix[left][right] = num

    return printMatrix(matrix)




print generateMatrix(0)
print generateMatrix(1)
print generateMatrix(2)
print generateMatrix(3)
print generateMatrix(4)
print generateMatrix(5)
