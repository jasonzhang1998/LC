# 最小的k个数
import heapq
from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0 or len(arr) == 0:
            return []
        heap = []
        for i in range(len(arr)):
            if i < k:
                heapq.heappush(heap, -arr[i])
            else:
                if -arr[i] > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -arr[i])
        res = []
        for _ in range(k):
            res.append(-heapq.heappop(heap))
        return res


if __name__ == '__main__':
    arr = [0, 1, 2, 1]
    print(Solution().getLeastNumbers(arr, 3))
