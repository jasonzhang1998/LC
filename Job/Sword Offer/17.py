# 打印从1到最大的n位数
from typing import List


class Solution:
    # 不考虑大数问题的解法
    def printNumber(self, n: int) -> List[int]:
        ans = []
        for i in range(1, 10 ** n):
            ans.append(i)
        return ans

    # 考虑大数问题，需要用字符串存储数，用字符串模拟加减法
    # 回溯法，用全排列的方法去实现加减法
    def printNumber2(self, n: int) -> List[str]:
        def dfs(index, nums, digit):
            # 如果到达最后一位，则将路径数组中的元素添加到答案中
            if index == digit:
                res.append(int("".join(nums)))
                return
            for j in range(10):
                # 没到末尾，将所有全排列加到路径数组中
                nums.append(str(j))
                # 计算下一位的全排列
                dfs(index + 1, nums, digit)
                # 回退操作
                nums.pop()

        res = []
        for i in range(1, n + 1):
            # first代表第一位的全排列，第一位不能为0
            for first in range(1, 10):
                nums = [str(first)]
                dfs(1, nums, i)
        return res


if __name__ == '__main__':
    print(Solution().printNumber(3))
