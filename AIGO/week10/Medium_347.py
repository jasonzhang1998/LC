# 前k个高频元素


# 先用哈希表存储各个元素对应的频次
# 再遍历k次哈希表，取出出现次数最大的元素(选择排序)
# 时间复杂度为O(kn)
import collections
import heapq


def topKFrequent(nums, k):
    n = len(nums)
    hash = {}
    for i in range(n):
        if nums[i] in hash:
            hash[nums[i]] += 1
        else:
            hash[nums[i]] = 1
    ans = []
    for i in range(k):
        for i, key in enumerate(hash):
            if i == 0:
                maxKey = key
            else:
                if hash[key] > hash[maxKey]:
                    maxKey = key
        ans.append(maxKey)
        hash.pop(maxKey)
    return ans


# 对哈希表进行桶排序
def topKFrequent2(nums, k):
    n = len(nums)
    hash = {}
    # 把元素及其出现次数存入哈希表
    for i in range(n):
        if nums[i] in hash:
            hash[nums[i]] += 1
        else:
            hash[nums[i]] = 1
    print("hash:", hash)
    bot = [[] for i in range(n + 1)]
    # 把元素按次数大小存入桶列表中
    for item in hash:
        bot[hash[item]].append(item)
    i = n - 1
    print("bot:", bot)
    i = n - 1
    ans = []
    while i > -1 and k > 0:
        if bot[i]:
            for j in bot[i]:
                ans.append(j)
                k -= 1
        i -= 1
    return ans


# 对哈希表进行堆排序
def topKFrequent3(nums, k):
    # n = len(nums)
    # hash = {}
    # for i in range(n):
    #     if nums[i] in hash:
    #         hash[nums[i]] += 1
    #     else:
    #         hash[nums[i]] = 1
    hash = collections.Counter(nums)
    print(hash)
    ans = []
    for key, value in hash.items():
        heapq.heappush(ans, (value, key))
        if len(ans) > k:
            heapq.heappop(ans)
    return [item[1] for item in ans]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums = [4, 1, -1, 2, -1, 2, 3]
    print(topKFrequent3(nums, 2))
