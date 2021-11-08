# 接雨水
from typing import List


class Solution:
    # 按行求累计的雨水, O(mn)，会超时
    def trap(self, height: List[int]) -> int:
        n = len(height)
        m = max(height)
        # ans[i]表示第i层累计的雨水数量
        ans = [0] * m
        # 累计雨水的高度不超过最高的柱子高度
        for i in range(1, m + 1):
            temp = 0
            # 标记是否更新temp
            isStart = False
            for j in range(n):
                if isStart and height[j] < i:
                    temp += 1
                # 只有当碰到第一个高度大于等于i的柱子，才开始更新temp
                if height[j] >= i:
                    ans[i - 1] += temp
                    temp = 0
                    isStart = True
        return sum(ans)

    # 按列求累计的雨水，O(n^2)，仍会超时
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for i in range(n):
            max_left = 0
            max_right = 0
            # 找出此列左边最高的柱子
            for j in range(0, i):
                max_left = max(max_left, height[j])
            # 找出此列右边最高的柱子
            for j in range(i + 1, n):
                max_right = max(max_right, height[j])

            # 计算能此列能累计的雨水
            temp = min(max_right, max_left)
            temp -= height[i]
            if temp > 0:
                ans += temp
        return ans

    # 基于前面按列计算的思路，将每列前面最高的柱子和后面做高的柱子存起来
    def trap3(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        right[n - 1] = height[n - 1]
        ans = 0
        # left[i]表示第i列前面最高的柱子高度
        # right[i]表示第i列后面最高的柱子高度
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])
        for i in range(1, n - 1):
            temp = min(left[i], right[i]) - height[i]
            if temp > 0:
                ans += temp
        print(left, '\n', right)
        return ans

    # 使用双指针对动态规划算法进行空间优化
    def trap4(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        max_left = height[0]
        max_right = height[n - 1]
        left = 1
        right = n - 2
        for i in range(1, n - 1):
            if max_left <= max_right:
                temp = max_left - height[left]
                if temp > 0:
                    ans += temp
                max_left = max(max_left, height[left])
                left += 1
            else:
                temp = max_right - height[right]
                if temp > 0:
                    ans += temp
                max_right = max(max_right, height[right])
                right -= 1
        return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap4(height))
