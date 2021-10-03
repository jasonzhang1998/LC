# 最大连续1的个数
from bisect import bisect
from typing import List


class Solution:
    # 对于任意的右端点 right，希望找到最小的左端点 left，
    # 使得 [left,right]包含不超过 k 个 0，
    # 枚举所有的右端点，找出满足条件的最长区间即为所求
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 构造前缀和数组，用于快速判断区间内0的个数，即p[right] - p[left - 1]
        p = [0]
        for i in range(n):
            p.append(p[-1] + (1 - nums[i]))
        print(p)
        ans = 0
        # 枚举所有的右端点，每次都找出最小的左端点
        for right in range(1, n + 1):
            l = 0
            r = right
            pivot = p[right] - k
            # 由于前缀和数组的单调递增的，因此可以使用二分查找最小左端点
            while l < r:
                mid = l + (r - l) // 2
                if p[mid] >= pivot:
                    r = mid
                else:
                    l = mid + 1
            # 记录每次的最大区间长度
            ans = max(ans, right - l)
        return ans

    # 观察到p[right] - k是递增的，因此p[left - 1]也是递增的
    # 因此可以通过滑动窗口来代替二分查找来寻找最小的左端点
    # 右端点不断右移，左端点从0开始，如果符合要求则不动
    # 不符合条件，则右移，直到符合条件。这样即是满足条件的最小左端点
    def longestOnes2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = lsum = rsum = 0
        ans = 0
        # 右端点不断右移
        for right in range(n):
            # 通过rsum变量来实时计算，此端点的前缀和数组值
            rsum += 1 - nums[right]
            # 如果不满足条件，则左端点右移
            while lsum < rsum - k:
                lsum += 1 - nums[left]
                left += 1
            # 取最大区间长度
            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    print(Solution().longestOnes2(nums, 2))
