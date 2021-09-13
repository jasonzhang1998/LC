# 机器人的运动范围


class Solution:
    # bfs搜索，一层层扫描可能到达的格子
    def movingCount(self, m: int, n: int, k: int) -> int:

        # 判断格子本身是否能得到
        def valid(i, j):
            row = i % 10 + i // 10
            col = j % 10 + j // 10
            if row + col <= k:
                return True
            return False

        from queue import Queue
        q = Queue()
        q.put((0, 0))
        ans = set()

        # bfs搜索
        while not q.empty():
            x, y = q.get()
            if (x, y) not in ans and 0 <= x < m and 0 <= y < n and valid(x, y):
                ans.add((x, y))
                for i, j in ((x + 1, y), (x, y + 1)):
                    q.put((i, j))
        return len(ans)


if __name__ == '__main__':
    print(Solution().movingCount(36, 11, 15))
