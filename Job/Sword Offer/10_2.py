# 青蛙跳台阶


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        pre = 1
        cur = 1
        ans = 0
        for i in range(n):
            ans = pre + cur
            pre = cur
            cur = ans
        return ans % int(1e9 + 7)


if __name__ == '__main__':
   print(Solution().numWays(8))