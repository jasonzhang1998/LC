'''
求背包问题的方案数
01背包问题，不是求在不超过背包容量的情况下装的最大价值，而是求装最大价值的方案数
'''
from typing import List


def selectionsCount(weights: List[int], values: List[int], cap) -> int:
    n = len(weights)
    mod = int(1e9 + 7)
    # dp[i][j]表示取前i个物品，不超过背包容量能取到的最大价值
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    # count[i][j]表示背包容量恰好为j时,得到最大价值的方案数
    count = [[0] * (cap + 1) for _ in range(n + 1)]
    count[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= weights[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

    for i in range(1, n + 1):
        for j in range(0, cap + 1):
            if dp[i][j] == dp[i - 1][j]:
                count[i][j] = (count[i][j] + count[i - 1][j]) % mod
            if j >= weights[i - 1] and dp[i][j] == dp[i - 1][j - weights[i - 1]] + values[i - 1]:
                count[i][j] = (count[i][j] + count[i - 1][j - weights[i - 1]]) % mod

    res = 0
    for j in range(cap + 1):
        if dp[n][j] == dp[n][cap]:
            res = (res + count[n][j]) % mod
    return res

# 空间优化
def selectionsCount2(weights: List[int], values: List[int], cap) -> int:
    n = len(weights)
    mod = int(1e9 + 7)
    # dp[j]表示不超过背包容量能取到的最大价值
    dp = [0] * (cap + 1)
    # count[j]表示背包容量恰好为j时,得到最大价值的方案数
    count = [0] * (cap + 1)
    count[0] = 1
    for i in range(1, n + 1):
        for j in range(cap, weights[i - 1] - 1, -1):
            tmp = max(dp[j], dp[j - weights[i - 1]] + values[i - 1])
            c = 0
            if tmp == dp[j]:
                c = (c + count[j]) % mod
            if tmp == dp[j - weights[i - 1]] + values[i - 1]:
                c = (c + count[j - weights[i - 1]]) % mod
            dp[j] = tmp
            count[j] = c

    res = 0
    for j in range(cap + 1):
        if dp[j] == dp[cap]:
            res = (res + count[j]) % mod

    return res


weights = [1, 2, 3, 4]
values = [2, 4, 4, 6]
cap = 5
print(selectionsCount2(weights, values, cap))
