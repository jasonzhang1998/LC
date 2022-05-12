# N皇后II

class Solution:
    def totalNQueens(self, n: int) -> int:
        # 回溯函数
        # 枚举所有皇后的位置，找出满足条件的方案
        def backtrack(index):
            # 找完所有符合条件的皇后了，记录答案并返回
            if index == n:
                self.ans += 1
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
        self.ans = 0
        # column，diagonal1和diagonal2用于判断棋子不能在同一列、和同一条斜线上
        # 由于回溯函数是每一行选一个皇后，所以不用判断是否处于同一行
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        # queens数组用于记录每一行的皇后的坐标，用于最后生成棋盘
        queens = [-1] * n
        backtrack(0)
        return self.ans


print(Solution().totalNQueens(3))
