# 最长连续序列
import collections
from typing import List


class Solution:
    # 先排序，再求连续的子序列，时间复杂度O(nlog(n))，不合题意
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        ans = 1
        start = nums[0]
        end = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1 or nums[i] == nums[i - 1]:
                end = nums[i]
            else:
                start = end = nums[i]
            ans = max(ans, end - start + 1)
        return ans

    # O(n)时间复杂度解法
    # 使用哈希表来判断某个元素是否存在
    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        ans = 1
        for num in nums:
            if num - 1 in nums:
                continue
            i = 1
            while num + i in nums:
                i += 1
            ans = max(ans, i)
        return ans


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2, 2]
    print(Solution().longestConsecutive2(nums))
