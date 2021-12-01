# 最长递增子序列
from typing import List


class Solution:
    # 动态规划：dp[i]表示以nums[i]为结尾元素的最长递增子序列长度
    # 时间复杂度O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 使用二分查找优化更新状态转移方程时候的遍历过程
    def lengthOfLIS2(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            if not dp or nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                n = len(dp)
                left, right = 0, n - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if nums[i] == dp[mid]:
                        break
                    elif nums[i] > dp[mid]:
                        left = mid + 1
                    elif nums[i] < dp[mid]:
                        right = mid - 1
                if nums[i] != dp[mid]:
                    dp[left] = nums[i]
        return len(dp)

    def lengthOfLIS3(self, nums: List[int]) -> int:

        dp = []
        for i in range(len(nums)):
            if not dp or nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                n = len(dp)
                left, right = 0, n
                while left < right:
                    mid = left + (right - left) // 2
                    if dp[mid] == nums[i]:
                        break
                    elif dp[mid] < nums[i]:
                        left = mid + 1
                    elif dp[mid] > nums[i]:
                        right = mid
                if dp[mid] != nums[i]:
                    dp[left] = nums[i]
        return len(dp)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 4]
    print(Solution().lengthOfLIS3(nums))
