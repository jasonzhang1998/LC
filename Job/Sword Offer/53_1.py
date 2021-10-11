# 在排序数组中查找数字I
from typing import List


class Solution:
    # 先二分查找，找到左边界，然后向右顺序遍历
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l = 0
        r = len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid
            elif nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
        # 没找到target值的情况，直接返回0
        if l == len(nums) or nums[l] != target:
            return 0
        count = 0
        while l < len(nums) and nums[l] == target:
            if nums[l] == target:
                count += 1
                l += 1
        return count


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 9]
    print(Solution().search(nums, 8))
