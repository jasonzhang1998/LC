# 买卖股票的最佳时机


# 算法思路：
# 使用两个变量pre和maxNum来存储最大利润时买入的价格，当前的最大利润
# 对于pre变量，遍历所有价格，如果遇到更低的价格，则在此时买入（保证买入最低的价格）
# 遍历所有价格时，每次都计算此时卖出时的利润。由于pre变量的定义，能够保证此时卖出
# 的利润是当前能产生的最大利润（因为pre变量一定是之前价格的最低点）
# 因此遍历一遍价格，求一遍在所有价格卖出时的最大利润，保存其中的最大值，即为所求
def maxProfit(prices):
    n = len(prices)
    if n < 2:
        return 0
    pre = prices[0]
    maxNum = 0
    for i in range(1, n):
        if prices[i] < pre:  # 更新股票的买入点
            pre = prices[i]
        elif prices[i] - pre > maxNum:
            maxNum = prices[i] - pre  # 更新最大利润
    return maxNum


if __name__ == '__main__':
    prices = [7, 6, 5, 4, 4, 4]
    print(maxProfit(prices))
