# n个骰子的点数
from typing import List


# 动态规划求解，第n个骰子的概率表由第n - 1个骰子的概率表转移得到
class Solution:
    # 逆向递推
    def dicesProbability(self, n: int) -> List[float]:
        # dp[n]代表第n个骰子的概率表
        dp = [[0] * (5 * n + 1) for _ in range(n + 1)]
        # 初始化第一个骰子的概率表
        for j in range(6):
            dp[1][j] = 1 / 6
        # 动态规划转移，一直到第n个骰子
        for i in range(2, n + 1):
            # 第i个骰子的概率表长度为5 * i + 1
            for j in range(5 * i + 1):
                # 每个骰子有6个值，因此可以前一个骰子的概率表的6项推导过来
                for k in range(6):
                    # 逆向递推的时候需要判断是否存在越界
                    if j - k >= 0:
                        dp[i][j] = dp[i][j] + dp[i - 1][j - k] / 6
                    else:
                        break
        res = dp[-1]
        return res

    # 正向递推
    def dicesProbability2(self, n: int) -> List[float]:
        dp = [[0] * (5 * n + 1) for _ in range(n + 1)]
        for j in range(6):
            dp[1][j] = 1 / 6
        for i in range(2, n + 1):
            for j in range(5 * (i - 1) + 1):
                for k in range(6):
                    dp[i][j + k] = dp[i][j + k] + dp[i - 1][j] / 6
        return dp[-1]


if __name__ == '__main__':
    print(Solution().dicesProbability2(2))
