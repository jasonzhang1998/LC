# 打家劫舍II
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 此函数是求打家劫舍的最高金额
        def dynamicProgramming(houses):
            n = len(houses)
            pre, cur, ans = 0, houses[0], houses[0]
            for i in range(1, n):
                ans = max(cur, pre + houses[i])
                pre = cur
                cur = ans
            return ans

        if len(nums) < 4:
            return max(nums)

        # 首尾连续的话，需要分偷第一家还是最后一家这两种情况
        return max(dynamicProgramming(nums[1:]), dynamicProgramming(nums[:-1]))
