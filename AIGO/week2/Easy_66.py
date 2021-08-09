# 加一


def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        digits[i] += 1
        digits[i] %= 10
        if digits[i] != 0:
            return digits
    digits = [0] * (n + 1)
    digits[0] += 1
    return digits


if __name__ == '__main__':
    print(plusOne([9, 9, 9]))
