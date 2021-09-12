# 斐波那契数列


class Solution:
    # 滚动数组版dp
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        pre = 0
        cur = 1
        ans = 1
        for i in range(1, n):
            ans = pre + cur
            pre = cur
            cur = ans
        return ans % int(1e9 + 7)

    # 递归，效率低下
    def fib2(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib2(n - 1) + self.fib2(n - 2)


if __name__ == '__main__':
    print(Solution().fib2(11))
    print(Solution().fib(11))
