# 统计花期内花的数目
import collections
from typing import List
import heapq


class Solution:
    # 从小到大遍历person的到达时间，如果有花开，那么则将其凋谢时间加入堆
    # 用堆来维护每朵花的凋谢时间，
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        times = sorted([(t, i) for i, t in enumerate(persons)])
        flowers.sort()
        heap = []
        ans = [0] * len(persons)
        j = 0
        for _, (t, i) in enumerate(times):
            # 将到达时间t及之前开的花(即t时间可能能看到的)，全部加入堆
            while j < len(flowers) and flowers[j][0] <= t:
                heapq.heappush(heap, flowers[j][1])
                j += 1
            # 将到达时间t之前凋谢的花(即t时间不能看到的花)，全部出堆
            while heap and heap[0] < t:
                heapq.heappop(heap)

            ans[i] = len(heap)
        return ans

    # 使用哈希表来表示某时刻开的花的数量,开花就加一，花谢就减一
    def fullBloomFlowers2(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        diff = collections.defaultdict(int)
        for start, end in flowers:
            diff[start] += 1
            diff[end + 1] -= 1
        times = sorted([(t, i) for i, t in enumerate(persons)])
        ans = [0] * len(times)
        keys = sorted(diff.keys())
        total = 0
        j = 0
        for _, (t, i) in enumerate(times):
            while j < len(keys) and keys[j] <= t:
                total += diff[keys[j]]
                j += 1
            ans[i] = total
        return ans


flowers = [[1, 10], [3, 3]]
persons = [3, 3, 2]

print(Solution().fullBloomFlowers2(flowers, persons))
