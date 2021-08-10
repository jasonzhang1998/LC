# 反转字符串


def reverseString(s):
    n = len(s)
    temp = None
    for i in range(n // 2):
        temp = s[i]
        s[i] = s[n - 1 - i]
        s[n - 1 - i] = temp
    return None


if __name__ == '__main__':
    s = ['h', 'e', 'l', 'l', 'o']
    print(reverseString(s))
    print(s)


