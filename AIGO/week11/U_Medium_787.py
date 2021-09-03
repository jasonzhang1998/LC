# k站中转内最便宜的航班
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
        pass


if __name__ == '__main__':
    x = Solution()
    n = 3
    edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    print(x.findCheapestPrice(n, edges, src, dst, k))