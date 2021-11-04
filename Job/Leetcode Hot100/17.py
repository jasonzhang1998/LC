# 电话号码的字母组合
from typing import List
from collections import deque


class Solution:
    # dfs回溯
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []
        path = []
        n = len(digits)

        def dfs(path, i):
            if i == n:
                ans.append(''.join(path))
                return
            char = digits[i]
            for item in dic[char]:
                path.append(item)
                dfs(path, i + 1)
                path.pop()

        dfs(path, 0)
        print(len(ans))
        return ans

    # 队列实现bfs
    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        s = ''
        q = deque()
        q.append(s)
        ans = []
        i, n = 0, len(digits)
        while q:
            if i == n:
                ans.append(q.popleft())
                continue
            k = len(q)
            for _ in range(k):
                s = q.popleft()
                for char in dic[digits[i]]:
                    c = s + char
                    q.append(c)
            i += 1
        return ans


if __name__ == '__main__':
    digits = '23'
    print(Solution().letterCombinations2(digits))
