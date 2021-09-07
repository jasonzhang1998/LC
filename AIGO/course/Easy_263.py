# 丑数


class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for i in [2, 3, 5]:
            while n % i == 0:
                n = n // i
        return n == 1


if __name__ == '__main__':
    print(Solution().isUgly(6))
