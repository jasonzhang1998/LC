# 买卖股票的最佳时机IV
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        n = len(prices)
        # dp[i][j][0]表示第i天结束时第j次买入股票的最大利润
        # dp[i][j][1]表示第i天结束时第j次卖出股票的最大利润
        dp = [[[0, 0] for _ in range(k)] for _ in range(n)]

        # 第一天买卖多少次都是一样的，都是买或者不买
        for j in range(k):
            dp[0][j][0] = -prices[0]
            dp[0][j][1] = 0

        for i in range(1, n):
            for j in range(k):
                if j == 0:
                    # 第一次买卖特殊处理
                    dp[i][j][0] = max(dp[i - 1][j][0], -prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i][j][0] + prices[i])
                else:
                    # 第i天不买卖则延续第i-1天的情况，如果买卖则需要转移
                    # 如果是第j次买入，则需要从第j-1次卖出的状态转移过来
                    # 如果是第j次卖出，则需要从第j次买入的状态转移过来
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] - prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i][j][0] + prices[i])
        return dp[n - 1][k - 1][1]