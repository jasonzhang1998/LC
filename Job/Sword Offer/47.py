# 礼物的最大价值
from typing import List


class Solution:
    # 动态规划思想
    # 滚动数组优化版本
    # 动态规划前，先考虑是否能够原地修改
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if not grid or m == 0 or n == 0:
            return 0
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[i % 2][j] = dp[i % 2][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + grid[i][j]
                else:
                    dp[i % 2][j] = max(dp[i % 2][j - 1], dp[(i - 1) % 2][j]) + grid[i][j]
        return dp[(m - 1) % 2][-1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().maxValue(grid))
