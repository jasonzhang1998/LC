# 寻找二维数组中的整数


def searchNum(matrix, target):
    # 判断输入的数组是否有效
    if not matrix or not matrix[0]:
        return None
    n, m = len(matrix), len(matrix[0])
    x, y = n - 1, 0
    while x >= 0 and y < m:
        num = matrix[x][y]
        if num == target:
            return [x, y]
        elif num > target:
            x -= 1
        else:
            y += 1
    return None


matrix = [[1, 3, 5],
          [2, 4, 6],
          [3, 6, 9]]

print(searchNum(matrix, 0))
print(searchNum(matrix, 1))
print(searchNum(matrix, 5))
print(searchNum([], 5))
