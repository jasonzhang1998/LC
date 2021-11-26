# 岛屿数量
from typing import List


class Solution:
    # dfs遍历
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if grid[x][y] == '0' or (x, y) in visited:
                return
            visited.add((x, y))
            for direc in direcs:
                newx = x + direc[0]
                newy = y + direc[1]
                if 0 <= newx < m and 0 <= newy < n:
                    dfs(newx, newy)
            return 1

        visited = set()
        direcs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if not dfs(i, j):
                    continue
                else:
                    count += 1
        return count


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(Solution().numIslands(grid))
