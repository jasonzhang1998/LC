# 找到小镇的法官


# 暴力遍历，假设每个人都是法官
def findJudge(n, trust):
    if n == 0:
        return -1
    if n == 1:
        return 1
    for i in range(1, n + 1):
        count = 0
        isJudge = True
        for item in trust:
            if item[0] == i:
                isJudge = False
                break
            if item[1] == i:
                count += 1
        if count == n - 1 and isJudge:
            return i
    return -1


# 将每个人视为一个节点，信任关系视为边，通过判断每个节点的入度和出度
# 来判断某个节点是不是法官
def findJudge2(n, trust):
    inDegree = [0] * n
    outDegree = [0] * n
    for i, j in trust:
        outDegree[i - 1] += 1
        inDegree[j - 1] += 1
    for i in range(n):
        if outDegree[i] == 0 and inDegree[i] == n - 1:
            return i + 1
    return -1


if __name__ == '__main__':
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    print(findJudge2(4, trust))
