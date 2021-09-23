# 调整数组顺序使奇数位于偶数前面
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # index之前的数全是奇数，index位为偶数
        index = 0
        for i in range(n):
            # 遇到奇数时与index位交换，偶数则跳过
            if nums[i] % 2 == 1:
                # 搜索index的初始点
                if index == i:
                    index += 1
                elif index < i:
                    # 交换
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
        return nums


if __name__ == '__main__':
    nums = [2, 1, 3, 4, 5, 6, 7]
    print(Solution().exchange(nums))
