# 最长回文子串


class Solution:
    # 中心拓展算法
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        n = len(s)
        max_length = 1
        for i in range(2 * n - 1):
            if i % 2 == 0:
                pre = i // 2 - 1
                pos = i // 2 + 1
            else:
                pre = i // 2
                pos = i // 2 + 1
            while pre >= 0 and pos < n:
                if s[pre] == s[pos]:
                    pre -= 1
                    pos += 1
                else:
                    break
            length = pos - pre - 1
            if length >= max_length:
                ans = s[pre + 1:pos]
                max_length = length
        return ans


if __name__ == '__main__':
    s = 'ac'
    print(Solution().longestPalindrome(s))
