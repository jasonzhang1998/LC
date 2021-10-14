# 和为s的连续正数序列
from typing import List


class Solution:
    # 滑动窗口
    # 滑动窗左右边界从头开始，tmp记录滑动窗口中的数之和
    # 只要右边界没有到达target，则不停止
    # 每次将tmp和target进行比较，如果相等，则将窗口中的元素加入答案
    # 如果tmp小了，则右边界右移，如果大了，这左边界右移
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        l, r = 1, 2
        tmp = l + r
        # while l < r < target:
        while l <= target // 2:
            if tmp == target:
                res.append([i for i in range(l, r + 1)])
                r += 1
                tmp += r
            elif tmp < target:
                r += 1
                tmp += r
            elif tmp > target:
                tmp -= l
                l += 1
        return res


if __name__ == '__main__':
    print(Solution().findContinuousSequence(15))
