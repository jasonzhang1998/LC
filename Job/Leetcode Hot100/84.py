# 柱状图中的最大矩形
from typing import List


class Solution:
    # 暴力搜索，从每个柱子出发，向两边延展，得到最大矩形
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0

        for i in range(n):
            left = i
            cur_height = heights[i]
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1

            right = i
            while right < n - 1 and heights[right + 1] >= cur_height:
                right += 1

            max_width = right - left + 1
            res = max(res, max_width * cur_height)
        return res

    # 单调栈，找到每根柱子两边第一个小于它的值
    def largestRectangleArea2(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        stack = []
        # 遍历每一根柱子
        for i in range(n):
            # 如果栈不为空，并且当前元素小于栈顶元素，则弹栈
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                # 计算弹栈元素的高度
                cur_height = heights[stack.pop()]

                # 将高度相等的元素弹栈，相邻的相等元素对应的矩形是一样的
                # 不去重也可以
                while len(stack) > 0 and cur_height == heights[stack[-1]]:
                    stack.pop()

                # 此时的栈顶元素是柱子左侧第一个小于当前柱子高度的柱子的索引
                # i是右侧第一个小于当前柱子高度的柱子的索引
                # 计算矩形宽度
                if len(stack) > 0:
                    cur_width = i - stack[-1] - 1
                else:
                    cur_width = i

                res = max(res, cur_width * cur_height)
            stack.append(i)

        # 遍历完一遍，若栈不为空，则需要把栈内元素都弹栈
        while len(stack) > 0:
            cur_height = heights[stack.pop()]
            while len(stack) > 0 and cur_height == heights[stack[-1]]:
                stack.pop()

            if len(stack) > 0:
                cur_width = n - stack[-1] - 1
            else:
                cur_width = n

            res = max(res, cur_width * cur_height)

        return res

    # 哨兵写法，列表左右各加一个高度为0的柱子
    def largestRectangleArea3(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        heights = [-1] + heights + [-1]
        stack = [0]
        n += 2
        for i in range(1, n):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_width * cur_height)
            stack.append(i)
        return res


if __name__ == '__main__':
    heights = [2, 1, 5, 3, 3, 3]
    print(Solution().largestRectangleArea2(heights))
