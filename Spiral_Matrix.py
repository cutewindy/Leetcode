# Given a matrix of m x n elements (m rows, n columns), 
# return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


def spiralOrder(matrix):
    order = []
    if matrix == []:
        return []
    # if len(matrix) == 1:
    #     return [matrix[0][i] for i in range(len(matrix[0]))]
    # if len(matrix[0]) == 1:
    #     return [matrix[i][0] for i in range(len(matrix))]
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            order.append(matrix[top][i])
        for i in range(top + 1, bottom):
            order.append(matrix[i][right])
        for i in reversed(range(left, right + 1)):
            if top < bottom:
                order.append(matrix[bottom][i])
        for i in reversed(range(top + 1, bottom)):
            if left < right:
                order.append(matrix[i][left])
        left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
    return order

print spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print spiralOrder([])
print spiralOrder([[]])
print spiralOrder([[1], [2]])
