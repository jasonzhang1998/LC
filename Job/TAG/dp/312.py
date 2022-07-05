# 戳气球
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j]表示戳开区间(i,j)的气球能得到的最大利润
        # dp[0][n - 1]为所求
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[j] * nums[k])
        return dp[0][n - 1]
