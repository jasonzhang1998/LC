# 队列的最大值
import queue


# 使用一个队列来实现插入和删除的O(1)复杂度，使用一个单调双端队列来实现获取最大值的O(1)复杂度
class MaxQueue:

    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    # 单调队列的队首元素为最大值
    def max_value(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1

    # 入队时，原队列直接入队，单调队列需要先把队列中小于value的元素排出来再入队
    def push_back(self, value: int) -> None:
        while self.deque and value > self.deque[-1]:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    # 出队时，原队列直接出队，单调队列需要判断出队元素是不是队首元素，如果是则出队
    def pop_front(self) -> int:
        if self.queue.empty():
            return -1
        value = self.queue.get()
        if value == self.deque[0]:
            self.deque.popleft()
        return value
