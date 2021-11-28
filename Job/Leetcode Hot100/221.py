# 最大正方形
import collections
from typing import List


class Solution:
    # 动态规划，dp[i][j]表示以(i, j)为右下角的矩形的最大边长
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if matrix[i][j] == '1':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:
                    if matrix[i][j] == '1':
                        # 动态转移方程，dp[i][j]为其左上方三个点的dp值的最小值加一
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    else:
                        dp[i][j] = 0
                res = max(dp[i][j], res)
        return res * res

    # 滚动数组优化空间复杂度
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(2)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    if matrix[i][j] == '1':
                        dp[i % 2][j] = 1
                    else:
                        dp[i % 2][j] = 0
                else:
                    if matrix[i][j] == '1':
                        dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[(i - 1) % 2][j - 1], dp[i % 2][j - 1]) + 1
                    else:
                        dp[i % 2][j] = 0
                res = max(res, dp[i % 2][j])
        return res ** 2


if __name__ == '__main__':
    matrix = [['1']]
    print(Solution().maximalSquare2(matrix))
