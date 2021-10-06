# 数据流中的中位数


from heapq import *


class MedianFinder:
    # 使用一个列表存储数据流，使用插入排序维持数组的有序
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return
        n = len(self.nums)
        # 使用插入排序来添加元素
        # for i in range(n):
        #     if self.nums[i] >= num:
        #         self.nums.insert(i, num)
        #         break
        # if self.nums[-1] < num:
        #     self.nums.append(num)

        # 由于数组有序，可以使用二分查找寻找插入位置进行优化
        # 但插入元素仍需要O(n)复杂度
        l = 0
        r = n
        while l < r:
            mid = l + (r - l) // 2
            if self.nums[mid] >= num:
                r = mid
            else:
                l = mid + 1
        self.nums.insert(l, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        i = n // 2
        if n % 2 == 1:
            return self.nums[i] / 1.0
        else:
            return (self.nums[i] + self.nums[i - 1]) / 2.0


class MedianFinder2:
    def __init__(self):
        # 小顶堆，保存较大的一半数
        self.A = []

        # 大顶堆，保存较小的一半数
        self.B = []

    def addNum(self, num: int) -> None:
        # 即元素数量为奇数,此时大根堆B需要添加一个元素
        # 需先将num插入A，然后A弹出最小元素，再将这个最小元素插入B
        # 为了模拟出大根堆，B的插入和弹出都需要对元素取反
        if len(self.A) != len(self.B):
            # heappush(self.A, num)
            # heappush(self.B, -heappop(self.A))

            # 使用heappushpop同时进行push和pop，提高效率
            heappush(self.B, -heappushpop(self.A, num))
        else:
            # 此时元素数量为偶数，A需要添加一个元素
            # 但是需要让元素先经过B，B弹出最大元素之后再插入A

            # heappush(self.B, -num)
            # heappush(self.A, -heappop(self.B))

            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self) -> float:
        if len(self.A) != len(self.B):
            return self.A[0] / 1.0
        else:
            return (self.A[0] - self.B[0]) / 2.0


if __name__ == '__main__':
    x = MedianFinder2()
    x.addNum(1)
    print(x.findMedian())
    x.addNum(2)
    # x.addNum(2)
    # x.addNum(4)
    # x.addNum(5)
    print(x.findMedian())
    print(x.A, x.B)
