# 不同路径2  (路径方格中有障碍物)
from typing import List


class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            if grid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        for i in range(m):
            if grid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[0, 1], [0, 0]]
    print(Solution().uniquePaths(grid))
