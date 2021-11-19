# 子集
from typing import List


class Solution:
    # 循环添加，迭代枚举
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            for i in range(len(ans)):
                temp = ans[i][:]
                temp.append(num)
                ans.append(temp)
        return ans

    # dfs回溯做
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            if index == n:
                return
            for i in range(index, n):
                path.append(nums[i])
                ans.append(path[:])
                dfs(i + 1, path)
                path.pop()

        n = len(nums)
        ans = [[]]
        path = []
        dfs(0, path)
        return ans


if __name__ == '__main__':
    nums = [1, 2]
    print(Solution().subsets2(nums))
