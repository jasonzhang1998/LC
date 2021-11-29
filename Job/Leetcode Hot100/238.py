# 除自身以外的数组的乘积
from typing import List


class Solution:
    # 使用一个前缀和数组和后缀和数组，对应的乘积即为所求。
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        pos = [0] * n
        for i in range(n):
            if i == 0:
                pre[i] = 1
                pos[n - i - 1] = 1
            else:
                pre[i] = pre[i - 1] * nums[i - 1]
                pos[n - i - 1] = pos[n - i] * nums[n - i]
        ans = [0] * n
        for i in range(n):
            ans[i] = pre[i] * pos[i]
        return ans

    # 使用两个变量来替代前缀和和后缀和数组，动态更新
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        pre = pos = 1
        for i in range(n):
            ans[n - i - 1] *= pos
            ans[i] *= pre
            pos *= nums[n - i - 1]
            pre *= nums[i]
        return ans


if __name__ == '__main__':
    nums = [3, 7, 5, 4]
    print(Solution().productExceptSelf2(nums))
