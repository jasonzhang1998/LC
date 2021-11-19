# 最大矩形
from typing import List


class Solution:
    # 将求最大矩形，转换为每行的柱形图最大矩形
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 求柱形图中的最大矩形
        def largestRectangle(heights):
            size = len(heights)
            res = 0
            heights = [-1] + heights + [-1]
            stack = [0]
            size += 2
            for i in range(1, size):
                while heights[i] < heights[stack[-1]]:
                    cur_height = heights[stack.pop()]
                    cur_width = i - stack[-1] - 1
                    res = max(res, cur_width * cur_height)
                stack.append(i)
            return res

        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        temp = [0] * n
        # 按每行求最大矩形，遍历所有的行
        for i in range(m):
            # 求每行对应的heights，heights[j]表示第i行第j列的元素上方连续的1的个数(包含自己)
            # 采用滚动数组优化，即每行的heights只与上一行有关
            for j in range(n):
                if matrix[i][j] == '0':
                    temp[j] = 0
                else:
                    temp[j] += 1
            # 对每行的柱状图求最大矩形，然后取最大值
            ans = max(ans, largestRectangle(temp))
        return ans


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(Solution().maximalRectangle(matrix))
