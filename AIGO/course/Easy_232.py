# 用栈实现队列


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        elif self.stack1:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
            return self.stack2.pop()
        else:
            return None

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
            return self.stack2[-1]
        else:
            return None

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


if __name__ == '__main__':
    ls = [1]
    print(ls[-1])
