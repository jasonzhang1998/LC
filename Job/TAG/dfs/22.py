# 括号生成
from typing import List


class Solution:
    # 可以把括号生成看作填一个长度为2*n的数组，每次可以填左右括号
    # 用dfs暴力枚举，2^(2*n)复杂度
    # 在填完之后判断是否有效，无剪枝
    def generateParenthesis(self, n: int) -> List[str]:
        # 判断一个括号字符数组是不是有效的
        def valid(chars):
            count = 0
            for c in chars:
                if c == '(':
                    count += 1
                else:
                    count -= 1
                if count > n or count < 0:
                    return False
            return count == 0

        # dfs
        def dfs(index, path):
            if index == 2 * n:
                if valid(path):
                    ans.append(''.join(path))
                return
            for item in ['(', ')']:
                path.append(item)
                dfs(index + 1, path)
                path.pop()

        ans = []
        dfs(0, [])
        return ans

    # 在递归生成的过程中进行剪枝，需要有两个剪枝条件
    def generateParenthesis2(self, n: int) -> List[str]:
        def dfs(path, left, right):
            if len(path) == 2 * n:
                ans.append(''.join(path))
                return

            # 当左括号数量达到n之后不再生成左括号
            if left < n:
                path.append('(')
                dfs(path, left + 1, right)
                path.pop()

            # 当左括号和右括号相等的时候不再生成右括号
            if left > right:
                path.append(')')
                dfs(path, left, right + 1)
                path.pop()

        ans = []
        dfs([], 0, 0)
        return ans


print(Solution().generateParenthesis2(3))
