# 电话号码的数字组合
from typing import List


class Solution:
    # 经典回溯，不需要任何剪枝
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, chars):
            if index == n:
                ans.append(''.join(chars))
                return
            s = dic[digits[index]]
            for c in s:
                chars.append(c)
                dfs(index + 1, chars)
                chars.pop()

        if not digits:
            return []
        dic = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        n = len(digits)
        ans = []
        dfs(0, [])
        return ans


string = "23"
print(Solution().letterCombinations(string))
