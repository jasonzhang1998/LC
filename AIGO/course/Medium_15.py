# 三数之和
from typing import List


class Solution:
    # 双指针法
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        # 先将列表排序
        nums.sort()
        print(nums)
        for i in range(n - 2):
            # 初始化前后指针
            j = i + 1
            k = n - 1
            # 如果这遍搜索的起点与之前相同，由于之前的搜索范围更大
            # 因此这遍搜索可以跳过，不用搜索
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                # 同上，跳过重复的搜索
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if k < n - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                    continue
                sumNum = nums[i] + nums[j] + nums[k]
                # 双指针不断靠近，搜索接近和为零的三个数
                if sumNum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif sumNum > 0:
                    k -= 1
                else:
                    j += 1
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
    # nums = [0, 0, 0]
    print(Solution().threeSum(nums))
