# 买卖股票的最佳时机含冷冻期
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i][0]表示第i天结束持有股票的最大利润
        # dp[i][1]表示第i天结束不持有股票且不处于冷冻期的最大利润
        # dp[i][2]表示第i天结束不持有股票且处于冷冻期的最大利润
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2])
            dp[i][2] = dp[i - 1][0] + prices[i]
        return max(dp[n - 1])
