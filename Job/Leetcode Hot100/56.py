# 合并区间
from typing import List


class Solution:
    # 先将区间按左边界排序，然后逐个合并
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        ans = []
        i = 0
        print(intervals)
        while i < n:
            while i < n - 1 and intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1][0] = intervals[i][0]
                intervals[i + 1][1] = max(intervals[i][1], intervals[i + 1][1])
                i += 1
            ans.append(intervals[i])
            i += 1
        return ans


if __name__ == '__main__':
    intervals = [[1, 4], [2, 3]]
    print(Solution().merge(intervals))
