# 判断子序列


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        m = len(s)
        n = len(t)
        j = 0
        for i in range(n):
            if j == m:
                return True
            if s[j] == t[i]:
                j += 1
        return j == m


if __name__ == '__main__':
    s = "ll8"
    t = "hello"
    print(Solution().isSubsequence(s, t))
