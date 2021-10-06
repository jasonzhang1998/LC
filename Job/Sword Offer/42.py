# 连续子数组的最大和
from typing import List


class Solution:
    # 从头开始累加数组元素
    # 如果之前的累加和小于等于0,意味着之前的累加是无用的
    # 这时重新开始累加,每轮累加之后记录最大的累加和
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curSum = float('-inf')
        ans = float('-inf')
        for i in range(len(nums)):
            if curSum <= 0:
                curSum = nums[i]
            else:
                curSum += nums[i]
            if curSum > ans:
                ans = curSum
        return ans


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
