# 组合总和
from typing import List


class Solution:
    # 本质是一个全排列问题，递归回溯解决
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # index 表示遍历的起点，用于去重，让选取点的时候不会去选index左边的元素
        def dfs(track, index, num):
            if num > target:
                return
            elif num == target:
                ans.append(track[:])
            else:
                for i in range(index, n):
                    # 稍微优化一下，减少回溯次数
                    if (num + candidates[i]) > target:
                        break
                    track.append(candidates[i])
                    num += candidates[i]
                    dfs(track, i, num)
                    num -= candidates[i]
                    track.pop()

        ans = []
        track = []
        n = len(candidates)
        candidates.sort()
        dfs(track, 0, 0)
        return ans


if __name__ == '__main__':
    nums = [2, 3, 5]
    print(Solution().combinationSum(nums, 8))
