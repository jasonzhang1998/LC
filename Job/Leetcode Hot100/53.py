# 最大子序和
from typing import List


class Solution:
    # 动态规划，dp[i]表示以nums[i]结尾的最大子序和，可以可以优化空间复杂度至O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)


if __name__ == '__main__':
    nums = [-2, -3]
    print(Solution().maxSubArray(nums))
