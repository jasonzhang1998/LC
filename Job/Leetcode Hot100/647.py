# 回文子串


class Solution:
    # 动态规划
    # dp[i][j]表示区间[i, j]的字符串是否为回文子串
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for j in range(n):
            for i in range(j + 1):
                # 状态转移方程
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
        return count

    # 中心扩展算法
    def countSubstrings2(self, s: str) -> int:
        count = 0
        n = len(s)
        # 总共有2n-1个中心点
        for i in range(2 * n - 1):
            # 初始化每次开始拓展时的左右指针
            left = i // 2
            right = left + i % 2
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count


if __name__ == '__main__':
    s = 'abc'
    print(Solution().countSubstrings2(s))
