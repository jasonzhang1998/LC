# 最长公共子序列


# 动态规划
# 状态定义：dp[i][j]表示text1的长度为i的前缀子串和text2的长度为j的前缀子串的最大公共子序列
# 状态转移：如果当前两个子串的最后一位相等，则dp[i][j] = dp[i-1][j-1] + 1
# 不相等，则取两个子串分别少一位之后的最大公共子序列的最大值
def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 0
    for i in range(n + 1):
        dp[0][i] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


# 由于dp[i][j]只与dp[i]和dp[i - 1]这两个数组的元素有关，
# 因此可以使用滚动数组进行空间优化
def longestCommonSubsequence2(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(2)]
    for i in range(n + 1):
        dp[0][i] = 0
    dp[1][0] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
            else:
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])
    return dp[m % 2][n]


if __name__ == '__main__':
    text1 = "intention"
    text2 = "execution"
    print(longestCommonSubsequence2(text1, text2))
