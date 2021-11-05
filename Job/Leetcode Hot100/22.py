# 括号生成
from typing import List


class Solution:
    # generate函数递归地暴力枚举所有可能的序列
    # valid函数判断序列是否有效
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A):
            # 递归终止条件，长度达到2n，有效的序列加入ans
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                # dfs遍历方式，包含回溯
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            # bal变量用于判断序列是否有效，其值为出现的左括号数量减去右括号数量
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                # 如果中途小于零，则无效
                if bal < 0:
                    return False
            # 如果最后不等于0也无效
            return bal == 0

        ans = []
        generate([])
        return ans

    # 递归生成所有的括号，但是在生成的过程中判断是否有效，无效的括号不会生成
    def generateParenthesis2(self, n: int) -> List[str]:
        ans = []

        def dfs(s, left, right):
            # 递归终止条件
            if len(s) == 2 * n:
                ans.append("".join(s))
                return

            # 左括号数为大于等于n之后，不会再添加左括号
            if left < n:
                s.append('(')
                dfs(s, left + 1, right)
                s.pop()

            # 右括号数和左括号数相等的时候，不会再添加右括号
            if left > right:
                s.append(')')
                dfs(s, left, right + 1)
                s.pop()

        dfs([], 0, 0)
        return ans

    # 动态规划求解，所有的序列的第一个字符肯定是'('，并且有一个')'与之对应
    # https://leetcode-cn.com/problems/generate-parentheses/solution/zui-jian-dan-yi-dong-de-dong-tai-gui-hua-bu-lun-da/
    def generateParenthesis3(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0].append("")
        for i in range(1, n + 1):
            for p in range(i):
                s1 = dp[p]
                s2 = dp[i - 1 - p]
                for k1 in s1:
                    for k2 in s2:
                        dp[i].append("({}){}".format(k1, k2))
        return dp[n]


if __name__ == '__main__':
    print(Solution().generateParenthesis3(3))
