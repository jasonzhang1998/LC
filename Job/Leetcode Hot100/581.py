# 最短无序连续子数组
from typing import List


class Solution:
    # 先排序，再找出首尾不一样的元素的下标
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tmp = sorted(nums)
        n = len(nums)
        for i in range(n):
            if tmp[i] != nums[i]:
                break
        for j in range(n - 1, -1, -1):
            if tmp[j] != nums[j]:
                break
        return j - i + 1 if i < j else 0

    # 两次遍历，寻找左右边界
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        right = 0
        left = 0
        maxnum = float('-inf')
        minnum = float('inf')
        n = len(nums)
        for i in range(n):
            if nums[i] >= maxnum:
                maxnum = nums[i]
            elif nums[i] < maxnum:
                right = i

        for j in range(n - 1, -1, -1):
            if nums[j] <= minnum:
                minnum = nums[j]
            elif nums[j] > minnum:
                left = j

        return 0 if right == left else right - left + 1


if __name__ == '__main__':
    nums = [1]
    print(Solution().findUnsortedSubarray2(nums))
