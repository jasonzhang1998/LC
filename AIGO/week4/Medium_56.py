# 合并区间


# 先将区间按区间的开始值大小进行排序，得到有序的区间，然后进行合并
def merge(intervals):
    n = len(intervals)
    ans = []
    intervals.sort(key=lambda x: x[0])
    print(intervals)
    i = j = 0
    while i < n and j < n:
        j = i + 1
        while j < n and intervals[j][0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[j][1], intervals[i][1])
            j += 1
        ans.append(intervals[i])
        i = j
    return ans


# 题解中更加优雅的写法
def merge2(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则的话，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == '__main__':
    intervals = [[1, 4], [0, 4], [8, 9]]
    print(merge2(intervals))
