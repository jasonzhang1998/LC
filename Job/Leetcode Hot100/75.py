# 颜色分类
import collections
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        dic = collections.Counter(nums)
        i, j = 0, dic[0]
        for k in range(n):
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
        for k in range(n):
            if nums[k] == 1:
                nums[j], nums[k] = nums[k], nums[j]
                j += 1


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    print(Solution().sortColors(nums))
    print(nums)
