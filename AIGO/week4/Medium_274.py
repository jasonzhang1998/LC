# H指数


# 首先将原数组按从大到小排序，然后根据定义遍历一遍找出H指数
def hIndex(citations):
    citations.sort(reverse=True)
    ans = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            ans = i + 1
    return ans


# 计数排序，先使用一个数组统计各个论文的引用次数，然后根据定义从高到到低累积判断H指数
def hIndex2(citations):
    n = len(citations)
    nums = [0] * (n + 1)
    for i in range(n):
        if citations[i] > n:
            nums[n] += 1
        else:
            nums[citations[i]] += 1
    count = 0
    for i in range(n, -1, -1):
        count += nums[i]
        if count >= i:
            return i


if __name__ == '__main__':
    citations = [3, 0, 1, 5, 6]
    print(hIndex2(citations))
