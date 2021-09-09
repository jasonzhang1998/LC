# Pow(x, n)


class Solution:
    # 递归实现，每次递归将n减半，直到n为0
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1.0
        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x * x, n // 2)

    # 迭代实现,注意将n为奇偶的情况分开
    def myPow2(self, x: float, n: int) -> float:
        index = n
        n = abs(n)
        if n == 0:
            return 1
        if n == 1:
            return x if index > 0 else 1.0 / x
        sumNum = 1
        while n > 1:
            if n % 2 == 0:
                x *= x
                n //= 2
            else:
                sumNum = sumNum * x
                n -= 1
        sumNum = sumNum * x
        return sumNum if index > 0 else 1.0 / sumNum


if __name__ == '__main__':
    print(Solution().myPow2(2, -1))
