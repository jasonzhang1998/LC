# 滑动窗口最大值
from typing import List


class Solution:
    # 暴力法，给滑动一下，遍历一次窗口，会超出时间限制
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            ans.append(max(nums[i:i + k]))
        return ans

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        pass


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(Solution().maxSlidingWindow(nums, 3))
