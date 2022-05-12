# N皇后
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 生成棋盘的函数
        # 根据queens数组中每行皇后的坐标来生成棋盘
        def generateboard():
            board = []
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board

        # 回溯函数
        # 枚举所有皇后的位置，找出满足条件的方案
        def backtrack(index):
            # 找完所有符合条件的皇后了，记录答案并返回
            if index == n:
                board = generateboard()
                solutions.append(board)
                return

            # 枚举这一行皇后的所有可选位置，进行回溯
            for i in range(n):
                # 如果在同一列或同一斜线则回溯
                if i in columns or index + i in diagonal1 or index - i in diagonal2:
                    continue
                queens[index] = i
                columns.add(i)
                diagonal1.add(index + i)
                diagonal2.add(index - i)
                backtrack(index + 1)
                columns.remove(i)
                diagonal1.remove(index + i)
                diagonal2.remove(index - i)

        # row用于最后生成棋盘
        row = ['.'] * n
        # column，diagonal1和diagonal2用于判断棋子不能在同一列、和同一条斜线上
        # 由于回溯函数是每一行选一个皇后，所以不用判断是否处于同一行
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        # queens数组用于记录每一行的皇后的坐标，用于最后生成棋盘
        queens = [-1] * n
        solutions = []
        backtrack(0)
        return solutions

    # 把集合改成位运算
    def solveNQueens2(self, n: int) -> List[List[str]]:
        # 生成棋盘的函数
        # 根据queens数组中每行皇后的坐标来生成棋盘
        def generateboard():
            board = []
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board

        def backtrack(index):
            if index == n:
                board = generateboard()
                solutions.append(board)
                return

            for i in range(n):
                bit1, bit2 = index - i + n, index + i
                if (self.columns >> i) & 1 == 1:
                    continue
                if (self.diagonal1 >> bit1) & 1 == 1:
                    continue
                if (self.diagonal2 >> bit2) & 1 == 1:
                    continue
                queens[index] = i
                self.columns |= 1 << i
                self.diagonal1 |= 1 << bit1
                self.diagonal2 |= 1 << bit2
                backtrack(index + 1)
                self.columns ^= 1 << i
                self.diagonal1 ^= 1 << bit1
                self.diagonal2 ^= 1 << bit2

        # row用于最后生成棋盘
        row = ['.'] * n
        self.columns = 0
        self.diagonal1 = 0
        self.diagonal2 = 0
        # queens数组用于记录每一行的皇后的坐标，用于最后生成棋盘
        queens = [-1] * n
        solutions = []
        backtrack(0)
        return solutions


print(Solution().solveNQueens2(4))
