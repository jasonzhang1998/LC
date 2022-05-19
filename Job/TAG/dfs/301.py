# 删除无效的括号
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(brackets):
            count = 0
            for i in range(len(brackets)):
                if brackets[i] == '(':
                    count += 1
                elif brackets[i] == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        level = {s}
        while True:
            valid = []
            for string in level:
                if is_valid(string):
                    valid.append(string)
            if valid:
                return valid
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i + 1:])
            level = next_level


s = "()())()"
print(Solution().removeInvalidParentheses(s))
