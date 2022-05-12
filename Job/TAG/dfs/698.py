# 划分为k个相等的子集
from typing import List


class Solution:
    # 球视角的回溯，每次决定把某个球放进哪个桶里
    # 时间复杂度为k的n次方，会严重超时
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        if target < max(nums):
            return False
        n = len(nums)
        nums.sort(reverse=True)
        bucket = [0] * n

        # index表示第index个小球
        def dfs(index):
            if index == n:
                for i in range(k):
                    if bucket[i] != target:
                        return False
                return True

            # 小球可以选择放入k个桶里
            for i in range(k):
                if bucket[i] + nums[index] > target:
                    continue
                bucket[i] += nums[index]
                if dfs(index + 1):
                    return True
                bucket[i] -= nums[index]
            return False

        return dfs(0)

    # 桶视角，从第一个桶开始，不停的放，如果放满了就放下一个桶
    # 时间复杂度为k * (2 ^ n)，还是会超时
    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        if target < max(nums):
            return False
        n = len(nums)
        nums.sort(reverse=True)
        used = [False] * n

        # curSum表示当前要放的桶的累计重量， k表示还剩下几个桶需要放
        def dfs(start, curSum, k):
            # k == 0和k == 1都可以，k == 1时，意味着只剩下一个桶要放了，把剩下的放进去就行
            if k == 1:
                return True

            # 放满了一个桶，此时需要放下一个桶
            # start从0开始寻找小球
            if curSum == target:
                return dfs(0, 0, k - 1)

            for i in range(start, n):
                if used[i]:
                    continue
                if curSum + nums[i] > target:
                    continue
                used[i] = True
                # start从i+1开始寻找后面的球
                if dfs(i + 1, curSum + nums[i], k):
                    return True
                used[i] = False
            return False

        return dfs(0, 0, k)

    # 在桶视角的基础上，加入记忆化搜索
    # 使用哈希表存储搜索到的状态的结果
    def canPartitionKSubsets3(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        if target < max(nums):
            return False
        n = len(nums)
        nums.sort(reverse=True)
        used = [False] * n
        dic = {}

        # curSum表示当前要放的桶的累计重量， k表示还剩下几个桶需要放
        def dfs(start, curSum, k):
            # k == 0和k == 1都可以，k == 1时，意味着只剩下一个桶要放了，把剩下的放进去就行
            if k == 1:
                return True

            if tuple(used) in dic:
                return dic[tuple(used)]

            # 放满了一个桶，此时需要放下一个桶
            if curSum == target:
                res = dfs(0, 0, k - 1)
                dic[tuple(used)] = res
                return res

            for i in range(start, n):
                if used[i]:
                    continue
                if curSum + nums[i] > target:
                    continue
                used[i] = True
                if dfs(i + 1, nums[i] + curSum, k):
                    return True
                used[i] = False
            return False

        return dfs(0, 0, k)

    # 使用used数组来表示状态会很占空间，可以使用二进制位来存储状态
    def canPartitionKSubsets4(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        if target < max(nums):
            return False
        n = len(nums)
        nums.sort(reverse=True)
        self.used = 0
        dic = {}

        def dfs(start, curSum, k):
            if k == 1:
                return True
            if self.used in dic:
                return dic[self.used]
            if curSum == target:
                res = dfs(0, 0, k - 1)
                dic[self.used] = res
                return res

            for i in range(start, n):
                if (self.used >> i) & 1 == 1:
                    continue
                if curSum + nums[i] > target:
                    continue

                self.used |= (1 << i)
                if dfs(i + 1, curSum + nums[i], k):
                    return True
                self.used ^= (1 << i)
            return False

        return dfs(0, 0, k)


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4

print(Solution().canPartitionKSubsets4(nums, k))
