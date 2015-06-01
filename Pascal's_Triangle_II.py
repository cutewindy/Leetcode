# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?

def getRow(rowIndex):
    row = [1]
    for i in range(1, rowIndex + 1):
        row = [1] + [row[j - 1] + row[j] for j in range(1, i)] + [1]
    return row

print getRow(3)