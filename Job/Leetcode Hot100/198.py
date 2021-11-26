# 打家劫舍
from typing import List


class Solution:
    # 动态规划思想，dp[i]表示以第i户人家结尾能偷到的最大财富
    # 对于每户人家，可以选择偷或者不偷即dp[i - 2] + nums[i]和dp[i - 1]
    # 取这两种情况的最大值即可
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]

    # 滚动数组版本
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        x, y, t = 0, nums[0], nums[0]
        for i in range(1, n):
            t = max(x + nums[i], y)
            x = y
            y = t
        return t


if __name__ == '__main__':
    nums = [1]
    print(Solution().rob2(nums))
