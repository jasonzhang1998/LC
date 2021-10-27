# 股票的最大利润
from typing import List


class Solution:
    # 贪心算法，使用变量buy记录股票的最低点，
    # 第i天卖出股票的最大最大利润为当天价格减去之前的股价最低点
    # 使用变量ans记录最大利润
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                continue
            ans = max(ans, prices[i] - buy)
        return ans


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
