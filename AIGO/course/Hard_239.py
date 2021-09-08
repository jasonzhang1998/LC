# 滑动窗口最大值
import collections
import heapq
from typing import List


class Solution:
    # 暴力法，给滑动一下，遍历一次窗口，会超出时间限制
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums) - k + 1):
            ans.append(max(nums[i:i + k]))
        return ans

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        # 将前k个元素加入大顶堆
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            # 每滑动一次,就将元素添加到堆中
            heapq.heappush(q, (-nums[i], i))
            # 如果此时的最大值不在滑动窗口内,则将其弹出
            # 直到出现的最大值在滑动窗口内,此时即为滑动窗内的最大值
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])
        return ans

    # 维持一个单调递减的双端队列,存放对应元素的索引值,每次队列的队首元素就是滑动窗口内的最大值
    # 使用collections.deque()能减小时间复杂度和空间复杂度,比用list实现性能更好
    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return None
        n = len(nums)
        window, ans = [], []
        # 初始化前k个元素的单调队列
        for i in range(k):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
        # 将对应最大值存入答案
        ans.append(nums[window[0]])
        # 向后移动滑动窗,每次加入一个元素,并维持队列的单调性,
        for i in range(k, n):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
            # 每次都判断队首元素是否在滑动窗口内,不在就出队
            while window[0] <= i - k:
                window.pop(0)
            # 每次取队首元素作为最大值加入答案
            ans.append(nums[window[0]])
        return ans


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    print(Solution().maxSlidingWindow3(nums, 3))
