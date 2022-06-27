# 分割回文串
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # f[i][j]表示s[i:j+1]是不是回文串
        f = [[True] * n for _ in range(n)]

        # 判读是否是回文串的条件是两端的元素相等
        # 并且子串也是回文串
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ans = []
        path = []

        # dfs回溯函数来枚举所有可能的分割方案
        # index表示剩下待分割子串的起始索引
        def dfs(index):
            if index == n:
                ans.append(path[:])
                return

            for j in range(index, n):
                if f[index][j]:
                    path.append(s[index:j + 1])
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans


print(Solution().partition("aab"))
