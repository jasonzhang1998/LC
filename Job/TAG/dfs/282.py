# 给表达式添加运算符
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []

        def backtrack(expr: List[str], i: int, res: int, mul: int):
            if i == n:
                if res == target:
                    ans.append(''.join(expr))
                return
            signIndex = len(expr)
            if i > 0:
                expr.append('')
            val = 0
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                val = val * 10 + int(num[j])
                expr.append(num[j])
                if i == 0:
                    backtrack(expr, j + 1, val, val)
                else:
                    expr[signIndex] = '+'
                    backtrack(expr, j + 1, res + val, val)
                    expr[signIndex] = '-'
                    backtrack(expr, j + 1, res - val, -val)
                    expr[signIndex] = '*'
                    backtrack(expr, j + 1, res - mul + mul * val, mul * val)
            del expr[signIndex:]

        backtrack([], 0, 0, 0)
        return ans


nums = '1234'
print(Solution().addOperators(nums, 6))
