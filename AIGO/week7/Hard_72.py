# 编辑距离


# 动态规划
# 状态定义：dp[i][j]表示word1长度为i的前缀和word2长度为j的前缀之间的最小编辑距离
# 状态转移：对于dp[i][j]，可以由dp[i - 1][j - 1]，dp[i][j - 1]，dp[i - 1][j]得到
# 因此只需考虑在前三种状态中选择最小的进行转移
def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1) + 1
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[m][n]


# 滚动数组思想进行空间优化
def minDistance2(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [[0] * (n + 1) for _ in range(2)]
    for i in range(n + 1):
        dp[0][i] = i
    for i in range(1, m + 1):
        for j in range(n + 1):
            if j == 0:
                dp[i % 2][j] = i
            else:
                if word1[i - 1] == word2[j - 1]:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[i % 2][j - 1], dp[(i - 1) % 2][j - 1] - 1) + 1
                else:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[i % 2][j - 1], dp[(i - 1) % 2][j - 1]) + 1
    return dp[m % 2][n]


if __name__ == '__main__':
    word1 = "hello"
    word2 = "happy"
    print(minDistance2(word1, word2))
