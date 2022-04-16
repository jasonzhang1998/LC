class Heap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self.float_up(len(self.heap) - 1)

    def heappop(self):
        if not self.heap:
            return None
        return_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sink_down(0)
        return return_item

    # 建堆操作
    # 将堆中的每个父节点都进行一次下沉操作
    def heapify(self, nums):
        self.heap = nums
        n = len(nums)
        print(self.heap)
        for i in reversed(range(n // 2)):
            self.sink_down(i)
            print(self.heap)

    # 上浮操作
    # 将数组最末尾的节点不断和其父节点交换，直至不能交换或到根节点
    def float_up(self, pos):
        item = self.heap[pos]
        while pos > 0:
            parent_pos = (pos - 1) >> 1
            parent = self.heap[parent_pos]
            if item < parent:
                self.heap[pos] = parent
                pos = parent_pos
                continue
            break
        self.heap[pos] = item

    # 下沉操作
    # 从某个父节点开始，一直和其子字节点交换，直至比它子节点均小或到达叶子节点
    def sink_down(self, pos):
        end_pos = len(self.heap)
        child_pos = 2 * pos + 1
        while pos < end_pos:
            right_pos = child_pos + 1
            if right_pos < end_pos and not self.heap[child_pos] < self.heap[right_pos]:
                child_pos = right_pos
            if child_pos < end_pos and self.heap[pos] > self.heap[child_pos]:
                self.heap[pos], self.heap[child_pos] = self.heap[child_pos], self.heap[pos]
                pos = child_pos
                child_pos = 2 * pos + 1
            else:
                break


if __name__ == '__main__':
    x = Heap()
    x.heapify([10, 7, 2, 5, 1])
    while x.heap:
        print(x.heappop())
    x.heappush(10)
    x.heappush(7)
    x.heappush(2)
    x.heappush(5)
    x.heappush(1)
