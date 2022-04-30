# 全排列
from typing import List


class Solution:
    # 填空型回溯，假设有长为n的数组，每次从nums中选一个数放入数组中
    # index表示待填的空的索引，path放已经填进去的数
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            # index为n表示已经填进去了n个数，此时记录答案，然后返回
            if index == n:
                ans.append(path[:])
                return
            # 每次可以所有数中选择一个数填进去
            for i in range(n):
                # 由于每个数只能填一次，因此当一个数被选过之后，就不能再选了
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(index + 1, path)
                    path.pop()

        # 交换型回溯，只需index参数，表示此时第index位的元素要和后面所有元素交换
        # 每次dfs中，index以前的位都固定了，不用动。

    def permute2(self, nums: List[int]) -> List[List[int]]:
        def dfs(index):
            # 表示前面n位元素都固定了，此时需记录答案并返回
            if index == n:
                # 此时经过交换之后的nums即为一种排列方案
                ans.append(nums[:])
                return

            # index之前的位都固定了，不用交换
            # 每次从index之后的元素选取一个和index处元素交换
            # index和自己交换也是一种方案
            for i in range(index, n):
                nums[i], nums[index] = nums[index], nums[i]
                dfs(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        n = len(nums)
        ans = []
        dfs(0)
        return ans


nums = [1, 2, 3]
print(Solution().permute2(nums))
