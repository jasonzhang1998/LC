# 目标和
from typing import List


class Solution:
    # 使用递归进行暴力枚举，会超时
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index, num):
            if index == n:
                if num == target:
                    self.count += 1
                return

            dfs(index + 1, num + nums[index])
            dfs(index + 1, num - nums[index])

        n = len(nums)
        self.count = 0
        dfs(0, 0)
        return self.count

    # 将问题优化成0-1背包问题
    # 动态规划求解
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        differ = sum(nums) - target
        n = len(nums)
        if differ < 0 or (differ & 1) == 1:
            return 0

        neg = differ >> 1
        dp = [[0] * (neg + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[n][neg]


if __name__ == '__main__':
    nums = [18, 50, 26, 2, 15, 14, 14, 2, 42, 43, 38, 44, 24, 17, 19, 25, 3, 10, 42, 20]
    print(Solution().findTargetSumWays2(nums, 24))
