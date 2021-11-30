# 寻找重复数
from typing import List


class Solution:
    # 从头开始遍历数组，如果该位置放着对应的数字，则跳过
    # 否则进行交换，把该位置的数字放到它该放的位置，然后继续判断
    # 如果发现要交换的数字对应的位置已经放好了，说明重复了，返回该数字
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == i + 1:
                continue
            else:
                while nums[i] != i + 1:
                    index = nums[i] - 1
                    if nums[index] == index + 1:
                        return nums[index]
                    nums[index], nums[i] = nums[i], nums[index]
        return nums[-1]


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 1]
    print(Solution().findDuplicate(nums))
