# 下一个排列
from typing import List


class Solution:
    # 将数组里的元素分为首尾两部分，后半部分为非递增序列，前半部分为剩余序列
    # 由于尾部的元素已经是递减(非严格)的了，所以需要把将首部变大一点点，然后把尾部变成最小
    # 所以算法可以分为以下三步：
    # 1、从后往前扫描，找到尾部和头部的分界点
    # 2、将头部的最尾元素，与尾部中刚好比它大的元素交换
    # 3、交换之后，尾部元素仍然是递减(非严格)的，所以需要反转尾部元素
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n < 2:
            return
        i = n - 1
        # 找出尾部最大的数，和要交换的头元素
        while i > 0:
            if nums[i - 1] >= nums[i]:
                i -= 1
            else:
                break

        # 如果整个排列是逆序的，则直接反转后返回
        if i == 0:
            nums.reverse()
            return

        # 用尾部比头元素大的最小数与头元素交换
        for j in range(n - 1, i - 1, -1):
            if nums[j] > nums[i - 1]:
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                break

        # 反转尾部元素
        left, right = i, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums = [3, 3, 1]
    Solution().nextPermutation(nums)
    print(nums)
