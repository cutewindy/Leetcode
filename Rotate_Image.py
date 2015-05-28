# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up:
# Could you do this in-place?

def rotate(matrix):
    n = len(matrix)
    if n < 2:
        return

    if n == 2:
        temp = matrix[0][0]
        matrix[0][0] = matrix[1][0]
        matrix[1][0]=matrix[1][1]
        matrix[1][1] = matrix[0][1]
        matrix[0][1] = temp
        return matrix
    
    for i in range(n/2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            matrix[j][n-i-1] = temp
    return matrix

print rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print rotate([[1, 2], [3, 4]])



