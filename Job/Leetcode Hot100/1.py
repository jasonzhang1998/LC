# 两数之和
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if (target - nums[i]) in dic:
                return [i, dic[target - nums[i]]]
            else:
                dic[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    print(Solution().twoSum(nums, 9))
