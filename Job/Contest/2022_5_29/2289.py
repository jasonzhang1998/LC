# 使数组按非递减顺序排列

from typing import List


class Solution:
    # 单调栈解法
    def totalSteps(self, nums: List[int]) -> int:
        ans, stack = 0, []
        for num in nums:
            max_t = 0
            while stack and stack[-1][0] <= num:
                max_t = max(max_t, stack.pop()[1])
            max_t = max_t + 1 if stack else 0
            ans = max(ans, max_t)
            stack.append((num, max_t))
        return ans



nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]

print(Solution().totalSteps(nums))