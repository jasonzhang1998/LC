# 三角形最小路径和


# 动态规划求解
def minTotal(triangle):
    m = len(triangle)
    # dp[i][j]表示到达点(i, j)的最小路径和
    dp = [[0] * m for _ in range(m)]
    # 初始化三角形的两条腰
    for i in range(m):
        if i == 0:
            dp[i][0] = triangle[i][0]
        else:
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
    for i in range(1, m):
        dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
    # 状态转移
    for i in range(2, m):
        for j in range(1, i):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    # 找出最小的路径和
    for i in range(m):
        if dp[m - 1][i] < dp[m - 1][0]:
            dp[m - 1][0] = dp[m - 1][i]
    return dp[m - 1][0]


# 优化一：原地修改，无需dp数组
def minTotal2(triangle):
    n = len(triangle)
    for i in range(1, n):
        triangle[i][0] += triangle[i - 1][0]
        for j in range(1, i):
            triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        triangle[i][i] += triangle[i - 1][i - 1]
    return min(triangle[n - 1])


# 优化二：由于每层dp数组值只与上一层有关，因此可以将n * n的dp数组优化为2 * n的数组
def minTotal3(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i % 2][0] = dp[(i - 1) % 2][0] + triangle[i][0]
        for j in range(1, i):
            dp[i % 2][j] = min(dp[(i - 1) % 2][j - 1], dp[(i - 1) % 2][j]) + triangle[i][j]
        dp[i % 2][i] = dp[(i - 1) % 2][i - 1] + triangle[i][i]
    return min(dp[(n - 1) % 2])


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(minTotal3(triangle))
