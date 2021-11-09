# 旋转图像
from typing import List


class Solution:
    # 根据旋转规律找出数字的赋值规律，然后由外向内进行旋转
    # 使用一个temp变量来保存交换的中间值
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        i = 0
        while i < n // 2:
            for j in range(i, n - 1 - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp
            i += 1


if __name__ == '__main__':
    matrix = [[1, 2], [3, 4]]
    print(Solution().rotate(matrix))
    print(matrix)
