# 爬楼梯


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        x = 1
        y = 1
        ans = 0
        for i in range(1, n):
            ans = x + y
            x = y
            y = ans
        return ans


if __name__ == '__main__':
    print(Solution().climbStairs(4))
