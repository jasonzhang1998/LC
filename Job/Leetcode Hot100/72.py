# 编辑距离


class Solution:
    # dp[i][j]表示word1前j个字符到word2前i个字符的编辑距离
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = i
        for i in range(n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word2[i - 1] == word1[j - 1]:
                    # 如果最后一个字母相同，那么问题可以转化为子问题
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 如果不同，那么可以转化为三个子问题
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


if __name__ == '__main__':
    word1 = 'intention'
    word2 = 'execution'
    print(Solution().minDistance(word1, word2))
