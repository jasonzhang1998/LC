# 子集II
# 即给定的数组里面有重复元素
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            # index表示选择的起点
            if index == n:
                return

            # 使用集合来剪枝，相同的元素不会被重复选择
            dic = set()
            for i in range(index, n):
                if nums[i] not in dic:
                    path.append(nums[i])
                    ans.append(path[:])
                    dic.add(nums[i])
                    dfs(i + 1, path)
                    path.pop()

        n = len(nums)
        ans = [[]]
        nums.sort()
        dfs(0, [])
        return ans

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            # index仍然是选择的起点
            if index == n:
                return

            for i in range(index, n):
                # 对同批次的选择来说，重复元素中只有第一个能进入dfs，其他的会被跳过
                if i > index and nums[i] == nums[i - 1] and not vis[i - 1]:
                    continue
                path.append(nums[i])
                ans.append(path[:])
                vis[i] = True
                dfs(i + 1, path)
                path.pop()
                vis[i] = False

        n = len(nums)
        ans = [[]]
        nums.sort()
        # 用一个vis数组来剪枝
        vis = [False] * n
        dfs(0, [])
        return ans


nums = [1, 2, 2]
print(Solution().subsetsWithDup2(nums))
