# 和为k的子数组
from typing import List


class Solution:
    # 暴力枚举, 会超时
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        return count

    # 前缀和 + 哈希表
    def subarraySum2(self, nums: List[int], k: int) -> int:
        count = 0
        pre = 0
        dic = {0: 1}
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in dic:
                count += dic[pre - k]
            dic[pre] = dic.get(pre, 0) + 1
        return count


if __name__ == '__main__':
    nums = [-1, -1, 1, 0]
    print(Solution().subarraySum(nums, 0))
