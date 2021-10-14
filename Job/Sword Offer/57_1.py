# 和为s的两个数字
from typing import List


class Solution:
    # 双指针从头尾向中间扫描
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        while i < j:
            tmp = nums[i] + nums[j]
            if tmp == target:
                return [nums[i], nums[j]]
            elif tmp > target:
                j -= 1
            else:
                i += 1


if __name__ == '__main__':
    nums = [10, 26, 30, 31, 47, 60]
    print(Solution().twoSum(nums, 40))
