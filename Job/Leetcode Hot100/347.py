# 前k个高频元素
import collections
import heapq
from typing import List


class Solution:
    # 先用哈希表统计频率，然后堆排序
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)
        heap = []
        for item in dic:
            heapq.heappush(heap, (dic[item], item))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        print(heap)
        for item in heap:
            ans.append(item[1])
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]
    print(Solution().topKFrequent(nums, 2))
