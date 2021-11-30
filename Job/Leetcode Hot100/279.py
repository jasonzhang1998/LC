# 完全平方数


class Solution:
    # 动态规划
    def numSquares(self, n: int) -> int:
        if n ** 0.5 == int(n ** 0.5):
            return 1
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[i - 1] + 1
            x = int((i + 1) ** 0.5)
            for j in range(1, x + 1):
                dp[i] = min(dp[i], dp[i - j ** 2])
            dp[i] += 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().numSquares(12))
