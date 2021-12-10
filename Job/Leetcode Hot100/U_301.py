# 删除无效的括号
from functools import lru_cache
from typing import List


class Solution:
    # BFS枚举，每删除一个括号，就判断剩下的括号是否合法
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        # BFS
        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level

    # dfs 遍历方法
    def removeInvalidParentheses2(self, s: str) -> List[str]:
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == ')':
                if l:
                    l -= 1
                else:
                    r += 1
        ans = []

        @lru_cache(None)
        def dfs(idx, cl, cr, dl, dr, path):
            if idx == len(s):
                if not dl and not dr:
                    ans.append(path)
                return
            if cr > cl or dl < 0 or dr < 0:
                return
            c = s[idx]
            if c == '(':
                dfs(idx + 1, cl, cr, dl - 1, dr, path)
            elif c == ')':
                dfs(idx + 1, cl, cr, dl, dr - 1, path)
            dfs(idx + 1, cl + (c == '('), cr + (c == ')'), dl, dr, path + c)

        dfs(0, 0, 0, l, r, "")
        return ans


if __name__ == '__main__':
    s = "()())()"
    print(Solution().removeInvalidParentheses2(s))
