# 最长有效括号


class Solution:
    # 动态规划算法
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)

        # dp[i]表示以s[i]结尾的最长的有效字符串的长度
        dp = [0] * n
        for i in range(1, n):
            # 以'('结尾的字符串肯定是无效的，只考虑以')'为结尾的字符串
            if s[i] == ')':
                # 如果前一位直接是'('，说明以该位为结尾的字符串肯定有效，直接加上之前的最大有效字符串长度
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                # 如果前一位是')'，则要考虑以该位为结尾的字符串是否
                else:
                    # 假设以前一位结尾的字符串是有效的，则跳过其有效字符串，找到其前一位，如果是'('
                    # 则说明以该位为结尾的字符串是有效的，最大长度为前一位的最大有效字符串加2，
                    # 再加上之前的有效部分长度
                    if (i - 1 - dp[i - 1]) >= 0 and s[i - 1 - dp[i - 1]] == '(':
                        dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
        return max(dp)


if __name__ == '__main__':
    s = '()(())))(('
    print(Solution().longestValidParentheses(s))
