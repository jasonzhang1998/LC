# 买卖股票的最佳时机3


# 动态规划
# 第i天的buy1表示到第i天结束，只进行一次买入操作，对本金产生的最大利润
# 第i天的sell1表示到第i天结束，进行一次买入和卖出操作后，对本金产生的最大利润
# 第i天的buy2表示到第i天结束，进行一次买入和卖出，再进行一次买入操作后，对本金产生的最大利润
# 第i天的sell2表示到第i天结束，进行两次买入和卖出操作后，对本金产生的最大利润
# 因此第i天结束后的sell2即为所求
def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    buy1 = -prices[0]
    sell1 = 0
    buy2 = -prices[0]
    sell2 = 0
    print(buy1, sell1, buy2, sell2)
    for i in range(1, n):
        # 第i天可以在之前买入过的情况下保持不变，也可以在没买过的情况下进行买入，
        # 通过取max来确定进行什么操作，即什么时候买入
        buy1 = max(buy1, -prices[i])

        # 第i天可以是之前卖出过一次之后保持不变，也可以是之前没卖过，今天卖出
        # 通过max来比较，哪天卖出获得的利润最大
        sell1 = max(sell1, buy1 + prices[i])

        # 转移方程同buy1相似，只是需要加上之前经过一次买卖之后所产生的利润sell1
        buy2 = max(buy2, sell1 - prices[i])

        # 转移方程与sell2相似，可以经过一次买卖后的sell1的转移方程
        sell2 = max(sell2, buy2 + prices[i])
        print(buy1, sell1, buy2, sell2)
    return sell2


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(maxProfit(prices))
