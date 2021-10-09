# 丑数
from heapq import *


class Solution:
    # 维护一个最小堆，里面存放所有的丑数，取第n个最小丑数
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]
        for i in range(n - 1):
            # 每次都弹出最小的丑数
            cur = heappop(heap)
            for factor in factors:
                num = cur * factor
                # 防止重复元素入堆
                if num not in seen:
                    seen.add(num)
                    heappush(heap, num)
        return heappop(heap)

    # 三指针动态规划，每个丑数都由之前的丑数乘2、3、5得来
    # 因此可以使用三个指针从头开始，通过指针不断后移，按从小到大的顺序产生丑数
    def nthUglyNumber2(self, n: int) -> int:
        dp = [1] * n
        a = b = c = 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if n2 == dp[i]:
                a += 1
            if n3 == dp[i]:
                b += 1
            if n5 == dp[i]:
                c += 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().nthUglyNumber2(955))
