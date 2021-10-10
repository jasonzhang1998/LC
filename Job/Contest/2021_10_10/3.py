# 股票波动价格
from heapq import *


# 使用一个哈希表和两个堆来存储数据
class StockPrice:

    def __init__(self):
        self.timestamp = {}
        self.latest = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
        # 哈希表存放时间戳和对应的价格
        self.timestamp[timestamp] = price

        # latest最大的时间戳，方便查找最新的股票价格
        self.latest = max(self.latest, timestamp)

        # 将所有数据都分别存放到一个小顶堆和大顶堆中
        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamp[self.latest]

    def maximum(self) -> int:

        # 从大顶堆中弹出一个元素，如果其价格和哈希表中对应的价格相等
        # 说明它是有效的价格，(即后续没有被更新过)，将其返回
        # 如果不等，则说明其价格无效，此时继续从大顶堆中弹出元素
        curprice, timestamp = heappop(self.maxHeap)
        while -curprice != self.timestamp[timestamp]:
            curprice, timestamp = heappop(self.maxHeap)

        # 弹出的元素需再次插入到堆中，维持队中有效的元素数量不变
        heappush(self.maxHeap, (curprice, timestamp))
        return -curprice

    def minimum(self) -> int:

        # 与查找最大值原理相同
        curprice, timestamp = heappop(self.minHeap)
        while curprice != self.timestamp[timestamp]:
            curprice, timestamp = heappop(self.minHeap)
        heappush(self.minHeap, (curprice, timestamp))
        return curprice


if __name__ == '__main__':
    x = StockPrice()
    x.update(1, 10)
    x.update(2, 5)
    print(x.current())
    print(x.maximum())
    x.update(1, 3)
    print(x.maximum())
    x.update(4, 2)
    print(x.minimum())
