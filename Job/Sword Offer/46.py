# 把数字翻译成字符串


class Solution:
    # 动态规划思想
    def translateNum(self, num: int) -> int:
        s = str(num)
        n = len(s)
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            x = int(s[i - 2]) * 10 + int(s[i - 1])
            if s[i - 2] == '0' or x > 25:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


if __name__ == '__main__':
    num = 506
    print(Solution().translateNum(num))
