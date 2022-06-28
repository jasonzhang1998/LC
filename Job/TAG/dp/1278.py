# 分割字符串III


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def cost(l, r):
            count, i, j = 0, l, r
            while i < j:
                count += (0 if s[i] == s[j] else 1)
                i += 1
                j -= 1
            return count

        n = len(s)
        # dp[i][j]表示把s的前i个字符分割成j个字符串需要修改的最少字符个数
        dp = [[10 ** 9] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                if j == 1:
                    dp[i][j] = cost(0, i - 1)
                else:
                    for i0 in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[i0][j - 1] + cost(i0, i - 1))

        return dp[n][k]
