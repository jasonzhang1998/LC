# 买卖股票的最佳时机III
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # buy1表示截至第i天只买过一次股票获得的最大利润
        # sell1表示截至第i天第一次卖出股票后获得的最大利润
        # buy2表示截至第i天第二次买入股票后获得的最大利润
        # sell2表示截至第i天第二次卖出股票后获得的最大利润
        buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0
        for i in range(1, n):
            # 今天买或者不买
            buy1 = max(buy1, -prices[i])
            # 今天卖或者不卖
            sell1 = max(sell1, buy1 + prices[i])
            # 今天买或者不买
            buy2 = max(buy2, sell1 - prices[i])
            # 今天卖或者不卖
            sell2 = max(sell2, buy2 + prices[i])
        return sell2
