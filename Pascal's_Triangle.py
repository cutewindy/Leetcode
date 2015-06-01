# Given numRows, generate the first numRows of Pascal's triangle.
# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(numRows):
    triangles = []
    for i in range(numRows):
        triangles.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                triangles[i].append(1)
            else:
                triangles[i].append(triangles[i-1][j-1] + triangles[i-1][j])
    return triangles

print generate(1)
print generate(2)
print generate(5)