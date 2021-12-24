# 分割等和子集
from typing import List


class Solution:
    # 将问题转换为0-1背包问题
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1 == 1 or len(nums) < 2:
            return False

        target = sum(nums) // 2
        n = len(nums)
        if max(nums) > target:
            return False

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True

        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    print(Solution().canPartition(nums))
