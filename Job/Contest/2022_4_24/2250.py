# 统计包含每个点的矩形数目

# 1 <= rectangles.length, points.length <= 5 * 104
# rectangles[i].length == points[j].length == 2
# 1 <= li, xj <= 109
# 1 <= hi, yj <= 100
# 所有rectangles互不相同。
# 所有points 互不相同。


import bisect
import collections
from typing import List


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        dic = collections.defaultdict(list)
        # 由于矩形的高度最多为100，因此可以根据高度将矩形分组
        # 然后在每个高度的矩形里面分别做二分
        for l, h in rectangles:
            dic[h].append(l)
        n = len(points)
        ans = [0] * n
        for h in dic.keys():
            # 对于每个矩形，先将其排序，然后遍历每个点
            # 如果点的高度符合要求，那么就进行二分
            dic[h].sort()
            for i in range(n):
                x, y = points[i]
                if y <= h:
                    index = bisect.bisect_left(dic[h], x)
                    ans[i] += len(dic[h]) - index
        return ans


rectangles = [[1, 2], [2, 3], [2, 5]]
points = [[2, 1], [1, 4]]

print(Solution().countRectangles(rectangles, points))
