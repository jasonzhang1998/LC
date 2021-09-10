# 二维数组中的查找
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(Solution().findNumberIn2DArray(matrix, 1))
