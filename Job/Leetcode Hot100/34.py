# 在排序数组中查找元素的第一个和最后一个位置
from typing import List


class Solution:
    # 二分搜索，搜索两次分别搜索上界和下界
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        n = len(nums)
        ans = []
        left, right = 0, n

        # flag变量用于判断是否找到
        flag = False

        # 寻找左侧边界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
                flag = True
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if flag:
            ans.append(left)
        else:
            ans.append(-1)
        left, right = 0, n

        # 寻找右侧边界
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if flag:
            # 非常重要，循环终止时left在右侧边界的后一位
            ans.append(left - 1)
        else:
            ans.append(-1)
        return ans


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    print(Solution().searchRange(nums, 7))
