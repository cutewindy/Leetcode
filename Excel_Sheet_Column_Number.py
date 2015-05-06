# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 

def titleToNumber(s):
    num = 0
    for i in s:
        num *= 26
        num += ord(i) - 64
    return num


print titleToNumber('A')
print titleToNumber('AA')
print titleToNumber("BA")