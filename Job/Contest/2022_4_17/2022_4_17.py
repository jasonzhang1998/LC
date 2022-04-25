from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        up = [[[0, 0] for _ in range(n)] for _ in range(m)]
        down = [[[0, 0] for _ in range(n)] for _ in range(m)]
        left = [[[0, 0] for _ in range(n)] for _ in range(m)]
        right = [[[0, 0] for _ in range(n)] for _ in range(m)]
        count = [[[0, 0] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                while x % 2 == 0:
                    count[i][j][0] += 1
                    x //= 2
                while x % 5 == 0:
                    count[i][j][1] += 1
                    x //= 5
                if i > 0:
                    up[i][j][0] = up[i - 1][j][0] + count[i - 1][j][0]
                    up[i][j][1] = up[i - 1][j][1] + count[i - 1][j][1]
                if j > 0:
                    left[i][j][0] = left[i][j - 1][0] + count[i][j - 1][0]
                    left[i][j][1] = left[i][j - 1][1] + count[i][j - 1][1]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                down[i][j][0] = down[i + 1][j][0] + count[i + 1][j][0]
                down[i][j][1] = down[i + 1][j][1] + count[i + 1][j][1]
                right[i][j][0] = right[i][j + 1][0] + count[i][j + 1][0]
                down[i][j][1] = down[i][j + 1][1] + count[i][j + 1][1]
        ans = 0
        for i in range(m):
            for j in range(n):
                c2 = up[i][j][0] + left[i][j][0] + count[i][j][0]
                c5 = up[i][j][1] + left[i][j][1] + count[i][j][1]
                ans = max(ans, min(c2, c5))
                c2 = up[i][j][0] + right[i][j][0] + count[i][j][0]
                c5 = up[i][j][1] + right[i][j][1] + count[i][j][1]
                ans = max(ans, min(c2, c5))
                c2 = down[i][j][0] + left[i][j][0] + count[i][j][0]
                c5 = down[i][j][1] + left[i][j][1] + count[i][j][1]
                ans = max(ans, min(c2, c5))
                c2 = down[i][j][0] + right[i][j][0] + count[i][j][0]
                c5 = down[i][j][1] + right[i][j][1] + count[i][j][1]
                ans = max(ans, min(c2, c5))
        return ans


nums = [[824, 709, 193, 413, 701, 836, 727], [135, 844, 599, 211, 140, 933, 205], [329, 68, 285, 282, 301, 387, 231],
        [293, 210, 478, 352, 946, 902, 137], [806, 900, 290, 636, 589, 522, 611], [450, 568, 990, 592, 992, 128, 92],
        [780, 653, 795, 457, 980, 942, 927], [849, 901, 604, 906, 912, 866, 688]]
print(Solution().maxTrailingZeros(nums))
