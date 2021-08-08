# 爬楼梯


# 直接递归（会超时）
def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n - 1) + climbStairs(n - 2)


# 动态规划
def climbStairs2(n):
    dp = {}
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n - 1]


# 滚动数组
def climbStairs3(n):
    p = 0
    q = 0
    k = 1
    for i in range(n):
        p = q
        q = k
        k = p + q
    return k


if __name__ == '__main__':
    print(climbStairs3(16))
    # for i in range(2, 5):
    #     print(i)
