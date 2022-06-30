# 买卖股票的最佳时机


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        ans = 0
        for i in range(1, n):
            # 维护最小的买入价格和历史的最大利润
            ans = max(ans, prices[i] - buy)
            buy = min(buy, prices[i])
        return ans
