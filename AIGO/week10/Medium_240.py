# 搜索矩阵2


# 类似二叉搜索树的思想，从左下方往右下方搜索
def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    i = m - 1
    j = 0
    if m == 0 or n == 0:
        return False
    while i > -1 and j < n:
        if target == matrix[i][j]:
            return True
        elif target > matrix[i][j]:
            j += 1
        else:
            i -= 1
    return False


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    print(searchMatrix(matrix, 5))
