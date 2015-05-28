# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# click to show follow up.

# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    dic = {}
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                dic[i] = j      
    for key, value in dic.items():
        for j in range(n):
            matrix[key][j] = 0
        for i in range(m):
            matrix[i][value] = 0
    return matrix
   

print setZeroes([[1,2,3],[2,0,3],[0,1,2]])
print setZeroes([[1, 2, 3, 0], [4, 0, 2, 1], [1, 3, 2, 0]])
print setZeroes([[0]])
print setZeroes([[3,5,5,6,9,1,4,5,0,5],[2,7,9,5,9,5,4,9,6,8],[6,0,7,8,1,0,1,6,8,1],[7,2,6,5,8,5,6,5,0,6],[2,3,3,1,0,4,6,5,3,5],[5,9,7,3,8,8,5,1,4,3],[2,4,7,9,9,8,4,7,3,7],[3,5,2,8,8,2,2,4,9,8]])







