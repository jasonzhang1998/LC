# 解数独
from typing import List


class Solution:
    # 使用line、column、block来进行判重剪枝
    # 预处理：找出所有待填的空格，并初始化line、column、block
    # 对所有空格进行回溯，枚举可填入的数字，然后递归回溯
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(pos):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return

        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        valid = False
        spaces = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)

    # 使用二进制位来代替状态数组
    def solveSudoku2(self, board: List[List[str]]) -> None:
        def dfs(pos):
            nonlocal valid
            if pos == len(spaces):
                return True

            i, j = spaces[pos]
            for digit in range(9):
                if ((line[i] >> digit) & 1) | ((column[j] >> digit) & 1) | ((block[i // 3][j // 3] >> digit) & 1) == 0:
                    line[i] |= 1 << digit
                    column[j] |= 1 << digit
                    block[i // 3][j // 3] |= 1 << digit
                    board[i][j] = str(digit + 1)
                    if dfs(pos + 1):
                        return True
                    line[i] ^= 1 << digit
                    column[j] ^= 1 << digit
                    block[i // 3][j // 3] ^= 1 << digit
            return False
        line = [0] * 9
        column = [0] * 9
        block = [[0] * 9 for _ in range(9)]
        valid = False
        spaces = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i] |= 1 << digit
                    column[j] |= 1 << digit
                    block[i // 3][j // 3] |= 1 << digit
        dfs(0)



