# 组合总和III
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # index表示已经选择的起点
        def dfs(index, path, total):
            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                return

            for i in range(index, 10):
                if total + i > n:
                    break
                path.append(i)
                dfs(i + 1, path, total + i)
                path.pop()

        ans = []
        dfs(1, [], 0)
        return ans
