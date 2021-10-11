# 0~n-1中缺失的数字
from typing import List


class Solution:
    # 二分查找
    # 缺失值以前的数字和它的下标相等，之后的数字大于其下标
    # 找出缺失值之后数字的左边界，这个边界数字的下标即为所求
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid
        return l


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 9]
    print(Solution().missingNumber(nums))
