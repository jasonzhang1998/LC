# 滑动窗口的最大值
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        queue = collections.deque()
        for i in range(n):
            while queue:
                if nums[i] >= nums[queue[-1]]:
                    queue.pop()
                else:
                    break
            queue.append(i)
            while i - queue[0] >= k:
                queue.popleft()
            if i >= (k - 1):
                ans[i - k + 1] = nums[queue[0]]
        return ans


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(Solution().maxSlidingWindow(nums, 3))
