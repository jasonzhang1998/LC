# 组合总和
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # index表示每次选择的起点，total表示累计的总数
        def dfs(index, path, total):
            if total == target:
                ans.append(path[:])
                return
            elif total > target:
                return

            # 为避免重复选择，需要每次从起点开始选数
            for i in range(index, n):
                # 剪枝，如果选某个元素已经超过target，后面的元素都不用选了
                if candidates[i] + total > target:
                    break
                path.append(candidates[i])
                # 这里的为什么是i，因为每个元素可以被重复选取，因此选过一次i之后，
                # 下次还能再选i
                dfs(i, path, total + candidates[i])
                path.pop()

        n = len(candidates)
        candidates.sort()
        ans = []
        dfs(0, [], 0)
        return ans
