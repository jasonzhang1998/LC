from typing import List


class Solution:
    # 将各个数往中间靠，这样的操作次数是最少的
    # 最后相等的数取中位数时，操作次数最少
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        arr = []
        if m * n == 1:
            return 0
        # 判断能否变成单值网格的方法是，任意两个数之差都能被x整除
        # 即某个数和其他数之差均能被x整除
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])
                if (grid[i][j] - grid[0][0]) % x != 0:
                    return -1
        arr.sort()
        # 取中位数
        mean = arr[m * n // 2]
        # 记录操作次数
        count = 0
        for i in range(m):
            for j in range(n):
                count += abs(mean - grid[i][j]) // x
        return count


if __name__ == '__main__':
    grid = [[529, 529, 989], [989, 529, 345], [989, 805, 69]]
    x = 9
    print(Solution().minOperations(grid, x))
