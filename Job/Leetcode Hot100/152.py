# 乘积最大子数组
from typing import List


# 动态规划思想：
# 需要维护最大值和最小值，因为最大值可能由之前的最大值、最小值和当前元素的得到。
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = preMin = preMax = nums[0]
        for i in range(1, n):
            curMax = max(preMax * nums[i], preMin * nums[i], nums[i])
            curMin = min(preMax * nums[i], preMin * nums[i], nums[i])
            preMax, preMin = curMax, curMin
            res = max(curMax, res)
        return res


if __name__ == '__main__':
    nums = [-4, -3, -2]
    print(Solution().maxProduct(nums))
