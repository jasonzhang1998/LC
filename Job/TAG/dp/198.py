# 打家劫舍
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]表示以偷完以前i户人家结尾的房屋的最高金额
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
        return dp[n]
