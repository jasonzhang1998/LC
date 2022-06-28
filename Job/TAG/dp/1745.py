# 分割字符串IV

class Solution:
    # 暴力枚举法，会超时
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        if n == 3:
            return True

        def isValid(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if isValid(0, i - 1) and isValid(i, j - 1) and isValid(j, n - 1):
                    return True
        return False

    # 提前通过动态规划预处理回文串的判断，平方复杂度
    def checkPartitioning2(self, s: str) -> bool:
        n = len(s)
        if n == 3:
            return True

        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

        for i in range(1, n - 1):
            for j in range(i + 1, n):
                if dp[0][i - 1] and dp[i][j - 1] and dp[j][n - 1]:
                    return True
        return False
