# 正则表达式匹配


class Solution:
    # 动态规划，dp[i][j]表示s[:i]和p[:j]是否匹配,最后返回结果是dp[m][n]
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 字符串为空，正则为空，能匹配
        dp[0][0] = True
        for i in range(m + 1):
            # j == 0时，即正则为空，此时除了字符串为空，其他时候均不匹配，因此值均为初始化的False
            for j in range(1, n + 1):
                # 如果正则元素此时不为*， 则判断此时值与字符串的值是否相等
                if p[j - 1] != '*':
                    # 如果i == 0，那么一定是不匹配的，若匹配，则p[j - 1]一定为 *
                    if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
                        # 若比较的值相等，则状态转移
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 此时正则元素为*，因为*不会单独出现，因此j一定大于等于2
                    # 如果此时字符串值与*前面一个值相等，那么则可以选择看或者不看
                    # 结果取或
                    if i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                        dp[i][j] = dp[i - 1][j] | dp[i][j - 2]
                    else:
                        # 如果值不相等，那么只能不看
                        # i == 0时，只能不看
                        dp[i][j] = dp[i][j - 2]
        return dp[-1][-1]


if __name__ == '__main__':
    s = 'abcd'
    p = 'd*'
    print(Solution().isMatch(s, p))
