# 栈的压入、弹出序列

from typing import List


class Solution:
    # 利用一个辅助栈，来模拟入栈出栈操作
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        i = j = 0
        stack = []
        while i < n:
            # 如果要弹出的数字不是栈顶元素，那么需要将入栈序列的元素入栈
            if len(stack) == 0 or popped[j] != stack[-1]:
                stack.append(pushed[i])
                i += 1
            # 如果栈顶元素是下一个要弹出的元素，则不断弹出该栈顶元素
            while len(stack) > 0 and j < n and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        # 所有元素入栈之后，判断是否已遍历完出栈序列
        return j == n

    # 更加高明简洁的实现
    def validateStackSequences2(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        # 每个元素入栈的时候，都循环判断是否该出栈
        for num in pushed:
            stack.append(num)  # num 入栈
            while stack and stack[-1] == popped[i]:  # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 1, 2, 3]
    print(Solution().validateStackSequences2(pushed, popped))
