# 最长递增子序列
from typing import List


class Solution:
    # 动态规划
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]表示以nums[i]结尾的最长递增子序列长度
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)