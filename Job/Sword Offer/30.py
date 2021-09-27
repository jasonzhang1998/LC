# 包含min函数的栈


# 使用一个辅助栈，用来存放数据栈此时每个元素为栈顶时对应的最小值
class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # 数据存入数据栈，对应的最小值存入辅助栈
    def push(self, x: int) -> None:
        self.stack1.append(x)
        # 如果辅助栈为空或者此时的新入元素小于原先的最小值，则放入辅助栈
        if len(self.stack2) == 0 or x < self.stack2[-1]:
            self.stack2.append(x)
        else:
            # 否则辅助栈的最小元素还是原来的最小值
            self.stack2.append(self.stack2[-1])

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def min(self) -> int:
        return self.stack2[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.stack2)
    print(float('inf'))