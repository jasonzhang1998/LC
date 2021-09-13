# 矩阵中的路径
from typing import List


class Solution:
    # 先bfs所有可能的起点，然后分别使用dfs搜索路径
    def exist(self, board: List[List[int]], word: str) -> bool:
        # board: List[List[int]], pos: tuple, word: str, visited: List[tuple], direc: List[tuple]
        def dfs(board, pos, word, visited, direc, bl):
            if len(word) == 1:
                return True
            for x in direc:
                i = pos[0] + x[0]
                j = pos[1] + x[1]
                if i in range(m) and j in range(n):
                    item = board[i][j]
                    if item == word[1] and (i, j) not in visited:
                        visited.append((i, j))
                        print('visited:', visited)
                        bl = dfs(board, (i, j), word[1:], visited, direc, bl)
                        if bl:
                            return True
                        visited.pop()
            return bl

        m = len(board)
        n = len(board[0])
        start = []
        visited = []
        bl = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append((i, j))
        print('start:', start)
        direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for pos in start:
            visited.clear()
            visited.append(pos)
            flag = dfs(board, pos, word, visited, direc, bl)
            if flag:
                return True
        return False

    # 简洁版的bfs + dfs
    def exist2(self, board: List[List[int]], word: str) -> bool:
        def dfs(i, j, k):
            if i not in range(m) or j not in range(n) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res = dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
            board[i][j] = word[k]
            return res

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False


if __name__ == '__main__':
    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    print(Solution().exist2(board, 'AAB'))
    print(board)
