# 盛最多水的容器
from typing import List


class Solution:
    # 暴力计算，会超时
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                if area > ans:
                    ans = area
        return ans

    # 双指针
    # 双指针首尾开始扫描，每次较小的指针向内移动
    # 因为较小的那个指针不可能再成为容器的边界了
    def maxArea2(self, height: List[int]) -> int:
        n = len(height)
        pre = 0
        pos = n - 1
        ans = 0
        while pre < pos:
            tmp = min(height[pre], height[pos]) * (pos - pre)
            if tmp > ans:
                ans = tmp
            if height[pre] > height[pos]:
                pos -= 1
            else:
                pre += 1
        return ans


if __name__ == '__main__':
    h = [2, 3, 4, 5, 18, 17, 6]
    print(Solution().maxArea2(h))
