'''
01背包问题，给定一系列物品的重量和价值，以及一个容量为l的背包
每个物品仅有一个，求在不超过背包容量的情况下，能装物品的最大价值。
'''
from typing import List

'''
动态规划思想：
dp[i][j]表示选前i个物品，容量不超过j的方案能装的最大价值
'''


def maxWeight(weights: List[int], values: List[int], cap) -> int:
    n = len(weights)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= weights[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
    return dp[n][cap]


'''
空间优化：由于dp[i][j]只和dp[i - 1]有关，因此可以用滚动数组优化
ps：由于状态转移方程涉及到之前的值，所以内层循环需要逆序
'''


def maxWeight2(weights: List[int], values: List[int], cap) -> int:
    n = len(weights)
    dp = [0] * (cap + 1)
    for i in range(1, n + 1):
        for j in range(cap, 0, -1):
            if j >= weights[i - 1]:
                dp[j] = max(dp[j], dp[j - weights[i - 1]] + values[i - 1])
    return dp[cap]


weights = [5, 4, 7, 2, 6]
values = [12, 3, 10, 3, 6]
cap = 7
print(maxWeight2(weights, values, cap))
