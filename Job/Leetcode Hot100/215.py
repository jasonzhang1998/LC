# 数组中的第k大的元素
import random
from typing import List
import heapq


class Solution:
    # 使用python内置的小根堆进行堆排序，求第k大的元素
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if i < k:
                continue
            heapq.heappop(heap)
        return heapq.heappop(heap)

    # 基于快排的topk元素
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # 划分算法，返回划分后标的pivot的下标index
        # index之前的数都小于pivot，之后的数都大于pivot
        def partition(alist, low, high):
            # 将任意元素与第一个元素交换
            index = random.randint(low, high)
            alist[index], alist[low] = alist[low], alist[index]
            pivot = alist[low]  # 选取第一个元素为标的
            while low < high:
                while low < high and alist[high] >= pivot:
                    high -= 1
                alist[low] = alist[high]
                while low < high and alist[low] <= pivot:
                    low += 1
                alist[high] = alist[low]
            alist[low] = pivot
            return low

        # 对数组进行递归划分，直到找到一个index，index之前的元素是前k-1小的元素
        def topk_split(alist, k, low, high):
            if low < high:
                index = partition(alist, low, high)
                if index == k:
                    return
                elif index < k:
                    topk_split(alist, k, index + 1, high)
                elif index > k:
                    topk_split(alist, k, low, index - 1)

        n = len(nums)
        topk_split(nums, n - k, 0, n - 1)
        return nums[n - k]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    print(Solution().findKthLargest2(nums, 2))
    # print(random.randint(0, 1))
