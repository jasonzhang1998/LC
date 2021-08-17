# 买卖股票的最佳时机2


# 贪心算法的思想
# 从头开始遍历，只要今天把股票卖出产生利润，那么就卖出，获得利润。
# 卖出之后再买入，到第二天再重复第一天的判断
def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    profit = 0
    for i in range(1, n):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
