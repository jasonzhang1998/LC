# 移动零
from typing import List


class Solution:
    # 冒泡移动
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        while left < right:
            while nums[left] == 0 and left < right:
                for i in range(left, right):
                    nums[i] = nums[i + 1]
                nums[right] = 0
                right -= 1
            print(nums)
            left += 1

    # 遇到非零元素就往前面填，填完之后后面补零
    def moveZeroes2(self, nums: List[int]) -> None:
        n = len(nums)
        pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
        while pos < n:
            nums[pos] = 0
            pos += 1


if __name__ == '__main__':
    nums = [1, 0, 0, 2, 3]
    Solution().moveZeroes2(nums)
    print("============")
    print(nums)
