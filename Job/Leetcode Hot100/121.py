# 买卖股票的最佳时机
from typing import List


class Solution:
    # 使用两个变量维护，最小的买入价格和最大的利润
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for num in prices:
            if num < buy:
                buy = num
            profit = max(profit, num - buy)
        return profit


if __name__ == '__main__':
    prices = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(prices))
