# 单词拆分
import collections
from typing import List


class Solution:
    # 自顶向下的计算
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(wordDict)
        starts = collections.deque()
        starts.append(0)
        while True:
            if not starts:
                return False
            n = len(starts)
            for i in range(n):
                for j in range(size):
                    word = wordDict[j]
                    num = len(word)
                    if word == s[starts[i]: starts[i] + num]:
                        # 这里非常重要，需要去重
                        if starts[i] + num not in starts:
                            starts.append(starts[i] + num)
                        if starts[i] + num == len(s):
                            return True
            for _ in range(n):
                starts.popleft()

    # 自底向上计算，枚举
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dic = collections.Counter(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    s = "cars"
    wordDict = ['car', 'ca', 'rs']
    print(Solution().wordBreak2(s, wordDict))
