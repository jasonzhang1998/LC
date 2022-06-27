# 统计放置房子的方式数

class Solution:
    # 只用看一侧的房子
    # 动态规划，每次放或者不放，类似打家劫舍
    def countHousePlacements(self, n: int) -> int:
        # dp[i]表示前i+1个位置放置房子的方式数
        dp = [2] * n
        dp[1] = 3
        mod = 10 ** 9 + 7
        for i in range(2, n):
            # 最后一个位置可以选择放或者不放
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod
        return dp[n - 1] ** 2 % mod
