# 值相等的最小索引
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i % 10 == nums[i]:
                return i
        return -1


if __name__ == '__main__':
    nums = [2, 1, 3, 5, 2]
    print(Solution().smallestEqual(nums))
