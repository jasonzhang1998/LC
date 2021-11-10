# 跳跃游戏
from typing import List


class Solution:
    # 自顶向下递归， 会超时
    def canJump(self, nums: List[int]) -> bool:
        def jump(index):
            if index == len(nums) - 1:
                return True
            if index > len(nums) - 1:
                return False
            temp = False
            for i in range(nums[index]):
                temp |= jump(index + i + 1)
            return temp

        return jump(0)

    # 自底向上，动态规划,时间复杂度很高
    def canJump2(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [False] * n
        dp[n - 1] = True
        for i in range(n - 2, -1, -1):
            step = nums[i]
            if step >= (n - 1 - i):
                dp[i] = True
                continue
            for j in range(1, step + 1):
                if i + j < n and dp[i + j]:
                    dp[i] = True
        return dp[0]

    # 贪心算法，从头遍历数组，维护最远可到达的位置
    # 如果最远能到达第i个位置，则第0到第i-1个位置都能到达
    def canJump3(self, nums: List[int]) -> bool:
        n = len(nums)
        max_pos = 0
        i = 0
        while i <= max_pos:
            max_pos = max(max_pos, i + nums[i])
            if max_pos >= n - 1:
                return True
            i += 1
        return False


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    print(Solution().canJump3(nums))
