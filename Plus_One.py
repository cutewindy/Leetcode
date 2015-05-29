# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.


def plusOne(digits):
    for i in reversed(range(len(digits))):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            break
    if digits[0] == 0:
        digits[0] = 1
        digits.append(0)
    return digits

print plusOne([9, 9])
print plusOne([2, 2, 1, 9, 0, 9])


def plusOneI(digits):
    carry = 1
    for i in reversed(range(len(digits))):
        sum = digits[i] + carry
        digits[i] = sum % 10
        carry = sum / 10
    if carry:
        digits = [1] + digits
    return digits

print plusOneI([9, 9])
print plusOneI([2, 2, 1, 9, 0, 9])




