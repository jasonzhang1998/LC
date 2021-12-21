# 戳气球
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        # 动态转移方程
        # 关键是要从小区间转移到大区间
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        return dp[0][n - 1]


if __name__ == '__main__':
    nums = [3, 1, 5, 8]
    print(Solution().maxCoins(nums))
