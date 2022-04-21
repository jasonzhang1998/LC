'''
求背包问题的具体方案
01背包问题，不是求在不超过背包容量的情况下装的最大价值，而是求装最大价值的具体方案
返回选取物品的序列编号，使得该序列的字典序最小
(字典序最小意味这需要按递增顺序返回编号，并且对于多种方案，尽量能选编号小的物品就选编号小的物品)
'''
from typing import List


def maxWeightSlection(weights: List[int], values: List[int], cap) -> List[int]:
    n = len(weights)
    # dp[i][j]表示在最后n - i个物品里面选，取得不超过背包容量的最大价值
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    # 注意外层循环的遍历顺序，是逆序遍历
    # 因为最好找具体方案的时候，物品得正着找，所以在算dp的时候要倒着算
    for i in range(n - 1, -1, -1):
        for j in range(cap + 1):
            dp[i][j] = dp[i + 1][j]
            if j >= weights[i]:
                dp[i][j] = max(dp[i][j], dp[i + 1][j - weights[i]] + values[i])
    ans = []
    cur = cap
    # 这里需要编号从小到大开始判断
    # 对于第i个物品，如果取它能得到最佳方案，则必取它
    for i in range(n):
        if cur >= weights[i] and dp[i][cur] == dp[i + 1][cur - weights[i]] + values[i]:
            ans.append(i + 1)
            cur -= weights[i]
    return ans


weights = [1, 2, 3, 4]
values = [2, 4, 4, 6]
cap = 5
print(maxWeightSlection(weights, values, cap))
