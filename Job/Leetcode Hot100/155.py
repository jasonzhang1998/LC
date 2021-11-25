# 最小栈


# 使用一个辅助栈，记录每个元素入栈时的最小值
# 由于辅助栈的操作和原栈一样，因此可以只用一个栈，存两个数据
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            min_num = self.stack[-1][1]
            if val < min_num:
                self.stack.append((val, val))
            else:
                self.stack.append((val, min_num))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
