from operator import add, sub, xor
from typing import List
# import queue
from collections import deque


class Solution:
    # BFS搜索,看找到goal的时候是搜索了几层
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque()
        q.append(start)
        seen = {start}
        i = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for num in nums:
                    for cand in (cur + num, cur - num, cur ^ num):
                        if cand == goal:
                            return i
                        elif 0 <= cand <= 1000 and cand not in seen:
                            q.append(cand)
                            seen.add(cand)
            i += 1
        return -1

    # 另一种bfs方式，将节点的值和其层数同时存到队列里
    def minimumOperations2(self, nums: List[int], start: int, goal: int) -> int:
        q = deque()
        seen = {start}
        q.append((start, 0))
        while q:
            val, step = q.popleft()
            if val == goal:
                return step
            if 0 <= val <= 1000:
                for num in nums:
                    for cand in (val + num, val - num, val ^ num):
                        if cand not in seen:
                            q.append((cand, step + 1))
                            seen.add(cand)
        return -1


if __name__ == '__main__':
    nums = [-21, 36, -12, 43, -4, -52, -93, 5, 12, 81, -90, 7, -31, -97, -49, 93, -65, 82, -37, 29, 87, -36, 70, 51, 60,
            -19, -73, -32, -13, -51, -23, 50]
    start = 4
    goal = 789
    print(Solution().minimumOperations2(nums, start, goal))
