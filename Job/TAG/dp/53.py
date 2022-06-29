# 最大子数组和
from typing import List


class Solution:
    # 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]表示以nums[i]结尾的最大子数组和
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)

    # 滚动数组优化空间复杂度
    def maxSubArray2(self, nums: List[int]) -> int:
        n = len(nums)
        cur = ans = nums[0]
        for i in range(1, n):
            if cur > 0:
                cur += nums[i]
            else:
                cur = nums[i]
            ans = max(ans, cur)
        return ans
