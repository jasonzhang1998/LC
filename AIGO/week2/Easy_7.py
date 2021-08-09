# 整数反转
def reverse(x):
    if x < 0:
        return -reverse(-x)
    ans = 0
    while x != 0:
        ans = x % 10
        x = x // 10
        ans = ans * 10 + ans
    return ans if ans < 2147483648 else 0


if __name__ == '__main__':
    print(reverse(-12355448))
    print(-12 // 10)
    print(pow(2, 31))
