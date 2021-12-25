# 找到所有数组中消失的数字
from typing import List


class Solution:
    # 使用一个辅助数组标记出现过的数字
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tmp = [0] * n
        for num in nums:
            tmp[num - 1] = 1
        ans = []
        for i in range(n):
            if tmp[i] == 0:
                ans.append(i + 1)
        return ans

    # 原地修改，在原数组上做标记
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            # 这里需要取模的原因是：有可能遍历到前面的元素时，后面的元素加了n
            # 遍历到后面时元素大小就大于n，因此会导致越界
            x = (num - 1) % n
            nums[x] += n
        ans = []
        for i in range(n):
            if nums[i] <= n:
                ans.append(i + 1)
            else:
                nums[i] %= n
        return ans


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers2(nums))
