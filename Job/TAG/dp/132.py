# 分割回文串II

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        # dp[i]表示以s[i]结尾的子字符串的最少分割次数
        dp = [n] * n
        for i in range(n):
            # 本身就是回文串，则不需要分割
            if f[0][i]:
                dp[i] = 0
            else:
                # 从前往后遍历找回文串
                for j in range(i):
                    if f[j + 1][i]:
                        # 遇到回文串就切割，取最小的切割方案
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[n - 1]


print(Solution().minCut("abc"))
