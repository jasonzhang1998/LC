# 每日温度
from typing import List


class Solution:
    # 暴力搜索， 会超时
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            for j in range(i, n):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans

    # 单调栈
    # 维护一个递减栈，如果新来的元素比栈顶元素大，则弹栈，得到栈顶元素的结果
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n):
            while stack and temperatures[i] > stack[-1][1]:
                item = stack.pop()
                index = item[0]
                ans[index] = i - index
            stack.append((i, temperatures[i]))
        return ans


if __name__ == '__main__':
    nums = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures2(nums))
