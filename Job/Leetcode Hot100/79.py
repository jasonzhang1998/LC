# 单词搜索
from typing import List


class Solution:
    # dfs搜索
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            # 如果字符不相等，则直接返回false
            if board[i][j] != word[k]:
                return False

            # 如果已经字符相等，并且已经到了单词末尾，则返回true
            if k == len(word) - 1:
                return True

            # visited记录每次搜索所经过的字符的坐标
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        # 只要四个方向有一个为true，则result为true
                        if check(newi, newj, k + 1):
                            result = True
                            break
            # 回溯操作
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))
