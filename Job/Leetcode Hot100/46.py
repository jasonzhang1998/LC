# 全排列
from typing import List


class Solution:
    # 经典回溯
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            if len(path) == n:
                ans.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs(path)
                    path.pop()

        n = len(nums)
        ans = []
        dfs([])
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))
