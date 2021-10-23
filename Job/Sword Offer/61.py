# 扑克牌中的顺子
from typing import List


class Solution:
    # 先排序，然后判断有无重复的非零元素，最后判断非零的最大值和最小值之差是否小于5
    def isStraight(self, nums: List[int]) -> bool:
        # 排序
        nums.sort()
        # 计算0的个数
        count = 0
        for num in nums:
            if num == 0:
                count += 1
        if count > 3:
            return True
        # 判断是否有重复元素
        for i in range(count, 4):
            if nums[i] ^ nums[i + 1] == 0:
                return False
        return (nums[4] - nums[count]) < 5

    # 更简洁的排序写法
    def isStraight2(self, nums: List[int]) -> bool:
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i + 1]:
                return False
        return nums[4] - nums[joker] < 5

    # 使用一个set来去重，用两个变量记录最大和最小值
    def isStraight3(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                continue
            elif num in repeat:
                return False
            else:
                mi = min(mi, num)
                ma = max(ma, num)
                repeat.add(num)
        return ma - mi < 5


if __name__ == '__main__':
    nums = [0, 4, 1, 2, 8]
    print(Solution().isStraight3(nums))
