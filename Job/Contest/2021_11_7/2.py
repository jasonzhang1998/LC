# 所有字符串中的元音

from typing import List


class Solution:
    # 动态规划、可以用滚动数组优化
    def countVowels(self, word: str) -> int:
        n = len(word)
        dp = [0] * n
        chars = ['a', 'e', 'i', 'o', 'u']
        dp[0] = 1 if word[0] in chars else 0
        for i in range(1, n):
            if word[i] in chars:
                dp[i] = dp[i - 1] + i + 1
            else:
                dp[i] = dp[i - 1]
        return sum(dp)


if __name__ == '__main__':
    word = 'aba'
    print(Solution().countVowels(word))
