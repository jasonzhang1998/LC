import heapq


def sortAD(ads):
    n = len(ads)
    dic = {}
    for ad in ads:
        if ad[1] not in dic:
            dic[ad[1]] = []
            heapq.heappush(dic[ad[1]], -ad[0])
        else:
            heapq.heappush(dic[ad[1]], -ad[0])
    pre = -1
    ans = []
    m = len(dic)
    nums = [0] * m
    for i in range(m):
        nums[i] = len(dic[i])
    for _ in range(n):
        maxNum = max(nums)
        res = n - len(ans)
        # 卡死的情况：必须选卡死的那类广告
        if res % 2 == 1 and maxNum == res // 2 + 1:
            index = 0
            for i in range(m):
                if nums[i] == maxNum:
                    index = i
        else:
            # 否则需要从与上次选取广告类别的不同的剩余广告中选择时间最长的
            for i in range(m):
                if nums[i] > 0:
                    index = i
                    break
            for j in range(m):
                if j == pre or not dic[j]:
                    continue
                if dic[j][0] <= dic[index][0]:
                    index = j
        item = -heapq.heappop(dic[index])
        ans.append((item, index))
        pre = index
        nums[index] -= 1
    return ans


if __name__ == '__main__':
    ads = [(100, 2), (32, 1), (54, 1), (100, 0), (49, 1), (73, 0), (10, 0)]
    ans = sortAD(ads)
    print(ans)
