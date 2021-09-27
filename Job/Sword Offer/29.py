# 顺时针打印矩阵
from typing import List


class Solution:
    # 按矩阵的层数，由外向内不断打印
    # 每次先确定待打印层的四个顶点
    # 然后按顺时针顺序不断打印
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        rows, columns = len(matrix), len(matrix[0])
        res = []
        # 选取初始打印时的四个顶点
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        # 这里的<=表示，只有一行或者一列，此时仍要打印
        while left <= right and top <= bottom:
            # 从左上到右上
            for column in range(left, right + 1):
                res.append(matrix[top][column])
            # 从右上到右下
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            # 当只有一行或一列的时候，无需重复打印
            if left < right and top < bottom:
                # 从右下到左下
                for column in range(right - 1, left, -1):
                    res.append(matrix[bottom][column])
                # 从左下到左上
                for row in range(bottom, top, -1):
                    res.append(matrix[row][left])
            # 进入下一层打印
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix = [[1, 2, 3, 4]]
    matrix = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]]
    print(Solution().spiralOrder(matrix))
    print(5 // 2)
