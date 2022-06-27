# 拼接数组的最大分数
from typing import List


class Solution:
    # 将问题转换为最大子数组和
    # 解法见 https://leetcode.cn/problems/maximum-score-of-spliced-array/solution/by-endlesscheng-fm8l/
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def solve(numsa, numsb):
            n = len(numsa)
            diff = [0] * n
            for i in range(n):
                diff[i] = numsb[i] - numsa[i]
            ans = 0
            cur = diff[0]
            for i in range(1, n):
                if cur > 0:
                    cur += diff[i]
                else:
                    cur = diff[i]
                ans = max(ans, cur)
            return ans + sum(numsa)

        return max(solve(nums1, nums2), solve(nums2, nums1))
