# 买卖股票的最佳时机II
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cur = prices[0]
        ans = 0
        for i in range(1, n):
            if prices[i] > cur:
                ans += prices[i] - cur
                cur = prices[i]
            else:
                cur = prices[i]
        return ans
