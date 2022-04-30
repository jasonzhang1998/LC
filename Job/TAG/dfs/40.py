# 组合总和II
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # index表示每次选择的起点，path记录路径，total记录总数
        def dfs(index, path, total):
            if total > target:
                return
            elif total == target:
                ans.append(path[:])
                return

            for i in range(index, n):
                if candidates[i] + total > target:
                    break
                # 不用vis数组也能剪枝，因为从i的选择范围就进行了判断
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, path, total + candidates[i])
                path.pop()

        n = len(candidates)
        ans = []
        candidates.sort()
        dfs(0, [], 0)
        return ans
