# 最小路径和


# 动态规划求解
def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    # dp[i][j]表示走到坐标（i, j）的点的最小路径和
    dp = [[0] * n for _ in range(m)]
    # 初始化第一行
    for i in range(m):
        if i == 0:
            dp[i][0] = grid[i][0]
        else:
            dp[i][0] = dp[i - 1][0] + grid[i][0]
    # 初始化第一列
    for i in range(n):
        if i == 0:
            dp[0][i] = grid[0][i]
        else:
            dp[0][i] = dp[0][i - 1] + grid[0][i]
    # 进行状态转移
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(minPathSum(grid))
