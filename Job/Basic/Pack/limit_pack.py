'''
多重背包：给定一系列物品的重量、价值和其能取的最大数量，以及一个容量为l的背包
求在不超过背包容量的情况下，能装物品的最大价值。
'''


from typing import List

'''
将多重背包问题分解为01背包问题，比如某个物品有一个，即最多可以取三次。可以转换为有三个同样的物品，每个物品可以取一次
这样即可以将多重背包转换成01背包，常用的是二进制分解法，即将物品的数量尽量分解成二进制表示
例如某个物品的数量为10，可以将其分解为1， 2， 4， 3
可以证明由1， 2， 4， 3的组合可以表示0～10的不同状态
'''


def maxWeight(weights: List[int], values: List[int],counts: List[int], cap) -> int:
    n = len(weights)
    # new_weights和new_values用来表示分解后的物品重量与价值
    new_weights = []
    new_values = []
    # 将每个物品的数量进行二进制分解
    for i in range(n):
        count = counts[i]
        j = 1
        while j < count:
            count -= j
            new_weights.append(weights[i] * j)
            new_values.append(values[i] * j)
            j *= 2
        if count > 0:
            new_weights.append(weights[i] * count)
            new_values.append(values[i] * count)
    n = len(new_weights)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= new_weights[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - new_weights[i - 1]] + new_values[i - 1])
    return dp[n][cap]


'''
空间优化：由于dp[i][j]只和dp[i - 1]有关，因此可以用滚动数组优化
ps：由于状态转移方程涉及到之前的值，所以内层循环需要逆序
'''


def maxWeight2(weights: List[int], values: List[int], counts, cap) -> int:
    n = len(weights)
    # new_weights和new_values用来表示分解后的物品重量与价值
    new_weights = []
    new_values = []
    # 将每个物品的数量进行二进制分解
    for i in range(n):
        count = counts[i]
        j = 1
        while j < count:
            count -= j
            new_weights.append(weights[i] * j)
            new_values.append(values[i] * j)
            j *= 2
        if count > 0:
            new_weights.append(weights[i] * count)
            new_values.append(values[i] * count)
    n = len(new_weights)
    dp = [0] * (cap + 1)
    for i in range(1, n + 1):
        for j in range(cap, 0, -1):
            if j >= new_weights[i - 1]:
                dp[j] = max(dp[j], dp[j - new_weights[i - 1]] + new_values[i - 1])
    return dp[cap]


weights = [1, 2, 3, 4]
values = [2, 4, 4, 5]
counts = [3, 1, 3, 2]
cap = 5
print(maxWeight2(weights, values, counts, cap))