# pow(x, n)


class Solution:
    # 递归计算
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return self.myPow(x, n - 1) * x

    # 迭代思想
    def myPow2(self, x: float, n: int) -> float:
        flag = n > 0
        n = abs(n)
        if n == 0:
            return 1
        if n == 1:
            return x if flag else 1. / x
        ans = 1
        while n > 0:
            if n % 2 == 0:
                x *= x
                n >>= 1
            else:
                ans = x * ans
                n -= 1
        return ans if flag else 1. / ans

    # 快速幂算法，将n转换成二进制，对应位上如果是1，那么就将ans与此时的x相乘，否则跳过
    def myPow3(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans


if __name__ == '__main__':
    print(Solution().myPow3(8.9, -1))
    if 1 + 1:
        print('true')
    if 1 - 1:
        print('false')
    while 1:
        print('sd')
