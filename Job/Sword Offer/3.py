# 数组中重复的数字
from typing import List


class Solution:
    # 用哈希表存放数字，遇到重复的就返回
    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash = {}
        for i in range(n):
            if nums[i] in hash:
                return nums[i]
            else:
                hash[nums[i]] = 1

    # 若非要追求空间复杂度，则可以先排序，这样重复的数组必相邻
    # 这样就可以通过异或运算判断是否重复
    def findRepeatNumber2(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] ^ nums[i + 1] == 0:
                return nums[i]

    # 原地置换算法
    def findRepeatNumber3(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            # 如果索引为i的位置的值已经是i了，那么就跳过到下一位
            if nums[i] == i:
                i += 1
                continue
            # 如果发现当前要替换的值，和它要被交换去到的位置上的值相同
            # 说明有两个相同的元素，此时返回这个值
            if nums[nums[i]] == nums[i]:
                return nums[i]
            # 如果当前索引i的值不为i，则把nums[i]放到它该去的位置
            # 找不到i的话，就会一直交换，直到出现碰撞
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


if __name__ == '__main__':
    nums = [2, 3, 1, 2, 5, 3]
    # nums = [3, 1, 2, 3]
    print(Solution().findRepeatNumber3(nums))
