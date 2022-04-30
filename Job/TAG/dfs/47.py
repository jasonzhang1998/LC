# 全排列II
# 即给定的数中有重复元素
from typing import List


class Solution:
    # 填空型回溯，由于数组本来就有重复的元素，因此除了满足每个元素只能填一次之外，
    # 还需要针对重复的元素进行去重
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            if index == n:
                ans.append(path[:])
                return
            # 每次还是从所有元素中选数填空
            for i in range(n):
                # 已经被选过的元素不能选
                if vis[i]:
                    continue
                # 重复的分支有两个特点：
                # 1、此时选择的元素和前面一个元素相同
                # 2、此时前一个元素没选择，即代表此元素取代了前一个元素的位置，
                # 意味着选择此元素之后的方案之前都已经遍历过了。
                # 此种方案只会遍历重复元素中选择第一个元素的所有方案，之后的元素会被排除
                # 如果把not vis[i]条件改为vis[i]，则每次只会遍历重复元素中选择最后一个元素的所有方案
                if i > 0 and nums[i] == nums[i - 1] and not vis[i - 1]:
                    continue
                path.append(nums[i])
                vis[i] = True
                dfs(index + 1, path)
                path.pop()
                vis[i] = False

        n = len(nums)
        ans = []
        # 为了保证相同的元素相邻，需要先对数组进行排序
        nums.sort()
        # vis数组用来标记某个元素是否已经选了
        vis = [False] * n
        dfs(0, [])
        return ans

    # 交换型回溯
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        def dfs(index):
            if index == n:
                ans.append(nums[:])
                return

            # 这里去除重复的元素的做法就是相同的元素不交换
            # 用dic记录交换到index位的所有数，如果重复了就不交换，跳过
            dic = set()
            for i in range(index, n):
                if nums[i] not in dic:
                    dic.add(nums[i])
                    nums[i], nums[index] = nums[index], nums[i]
                    dfs(index + 1)
                    nums[index], nums[i] = nums[i], nums[index]

        n = len(nums)
        ans = []
        dfs(0)
        return ans


nums = [1, 2, 1]
print(Solution().permuteUnique2(nums))
