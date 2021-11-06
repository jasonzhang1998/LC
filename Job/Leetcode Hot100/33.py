# 搜索旋转排序数组
from typing import List


class Solution:
    # 二分搜索
    # 将nums分为前后两部分，前半部分的数都大于后半部分的数
    # 二分搜索的时候，前通过和端点值的比较确定mid在前半部分还是后半部分
    # 然后再和target比较，确定target在mid之前还是之后
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= max(nums[left], nums[right]):
                if nums[mid] == target:
                    return mid
                elif target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right -= 1
            else:
                if nums[mid] == target:
                    return mid
                elif target < nums[mid] or target > nums[right]:
                    right -= 1
                else:
                    left += 1
        return -1


if __name__ == '__main__':
    nums = [3, 1]
    target = 1
    print(Solution().search(nums, target))
