# 滑动窗口的最大值
from typing import List


class Solution:
    # 使用一个长度为k的滑动窗去模拟最大值的计算过程
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 1:
            return nums
        res = []
        ans = []
        for i in range(k):
            res.append(nums[i])
        ans.append(max(res))
        for i in range(k, len(nums)):
            res.append(nums[i])
            res.pop(0)
            ans.append(max(res))
        return ans

    # 使用单调队列来求滑动窗的最大值
    # 维护一个元素值单调递减的列表window，window里面存放元素的索引
    # 每次遍历到一个元素时，需要做两件事
    # 第一，比较该元素和列表末尾元素的大小，如果该元素大，则末尾元素需弹出
    # 直到末尾元素比该元素大，或者window为空。然后将该元素插入window末尾
    # 这样做的原因是：当遍历到该元素时，window里面存在的元素都是该元素之前的元素，
    # 如果这些元素比该元素小，那么这些元素再也不可能是滑动窗里面的最大值了，因此需要弹出
    # 第二，判断window头部元素是否还在窗口内，如果不在则需弹出，判断方法是计算该元素的索引
    # 与当前遍历元素的索引之间的差值是否大于等于k。然后将window的头部元素存入res
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 1:
            return nums
        n = len(nums)
        window = []
        res = []
        for i in range(n):
            # 维持window的单调递减性
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
            # 元素都放进遍历到第k个元素时，需要计算最大值了
            if i >= k - 1:
                # 移除window中滑动窗之外的元素
                while i - window[0] >= k:
                    window.pop(0)
                res.append(nums[window[0]])
        return res


if __name__ == '__main__':
    nums = [7, 2, 4]
    print(Solution().maxSlidingWindow2(nums, 2))
