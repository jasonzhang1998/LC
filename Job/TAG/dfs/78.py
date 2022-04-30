# 子集
from typing import List


class Solution:
    # dfs回溯
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            # index表示的是本次能选择的元素的起点
            # index为n表示从一个不存在的元素作为起点，此时需要直接返回
            if index == n:
                return
            # 每次只能从起点开始往后面选择
            for i in range(index, n):
                # path添加一个元素，代表做了一次选择
                path.append(nums[i])
                # 每次做一个选择之后就需要记录下此时的路径
                ans.append(path[:])
                dfs(i + 1, path)
                path.pop()

        n = len(nums)
        # 空子集需要单独添加
        ans = [[]]
        dfs(0, [])
        return ans

    # 迭代枚举
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            for i in range(len(ans)):
                temp = ans[i][:]
                temp.append(num)
                ans.append(temp)
        return ans


nums = [1, 2, 3]
print(Solution().subsets2(nums))
