# 零钱兑换
import functools
from typing import List


class Solution:
    # 递归 + 记忆化搜索，
    def coinChange(self, coins: List[int], amount: int) -> int:
        # lru_cache能让相同的输入直接返回结果避免重复计算
        @functools.lru_cache(amount)
        def helper(num):
            if num == 0:
                return 0
            elif num < 0:
                return -1
            minCoins = float('inf')
            for coin in coins:
                temp = helper(num - coin)
                if 0 <= temp < minCoins:
                    minCoins = temp + 1
            return minCoins if minCoins < float('inf') else -1

        # self.coins = coins
        return helper(amount)

    # 自底向上，动态规划
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] < float('inf') else -1


if __name__ == '__main__':
    coins = [186, 419, 83, 408]
    # coins = [1, 2, 5]
    print(Solution().coinChange2(coins, 6249))
