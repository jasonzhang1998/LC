# 使用最小花费爬楼梯


# 动态规划
# dp[i]表示爬到第i阶台阶，并往上爬的最小花费
def minClimbing(cost):
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
    return min(dp[n - 1], dp[n - 2])


# 滚动数组实现动态规划
def minClimbing2(cost):
    n = len(cost)
    x = cost[0]
    y = cost[1]
    t = 0
    for i in range(2, n):
        t = min(x, y) + cost[i]
        x = y
        y = t
    return min(x, y)


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(minClimbing(cost))
