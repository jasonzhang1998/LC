# 前k个高频单词
import collections
import heapq
from typing import List


# 先用哈希表取出频率,后用排序,然后取前k个元素
class Solution(object):
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash = collections.Counter(words)
        tmp = []
        for key, value in hash.items():
            tmp.append((value, key))
        # 这里的lambda函数非常关键,-x[0]表示value,从大到小排列
        # x[1]表示key从小到大排列,这样就兼顾了频率由高到低,字典
        # 序由低到高
        ans = sorted(tmp, key=lambda x: (-x[0], x[1]))
        print(ans)
        return [item[1] for item in ans[:k]]

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        hash = collections.Counter(words)
        ans = []
        for key, value in hash.items():
            # 这里采用词频的负值入堆,与上个排序方法思路一样
            heapq.heappush(ans, (-value, key))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(ans)[1])
        return res

    # 使用堆排序,通过重写小于运算符来使得顺序符合题意
    def topKFrequent3(self, words: List[str], k: int) -> List[str]:
        hash = collections.Counter(words)
        ans = []
        for key, value in hash.items():
            heapq.heappush(ans, Word(key, value))
            if len(ans) > k:
                heapq.heappop(ans)
        ans.sort(reverse=True)
        return [item.key for item in ans]


# 重写两个元素大小的比较方法
class Word:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    # 重写小于运算符
    def __lt__(self, other):
        # 两个元素的value值相同,则key大的元素大
        if self.value == other.value:
            # key大的元素反而小
            return self.key > other.key
        else:
            # value小的元素小
            return self.value < other.value


if __name__ == '__main__':
    words = ["i", "love", "leetcode", "love", "i", "coding"]
    x = Solution()
    result = x.topKFrequent3(words, 3)
    print(result)
