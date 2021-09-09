# 不同路径


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(2)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i % 2][j] = 1
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + dp[i % 2][j - 1]
        return dp[(m - 1) % 2][n - 1]


if __name__ == '__main__':
    print(Solution().uniquePaths2(3, 7))
    print([[0] * 3 for _ in range(5)])
    print([[0 for _ in range(3)] for _ in range(7)])
