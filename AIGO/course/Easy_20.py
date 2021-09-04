# 有效的括号


class Solution:
    # 由于左右括号具有对应关系，其实可以用一个hashmap来存
    # 这样就少写一些括号和if else
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item in ['(', '[', '{']:
                stack.append(item)
            elif item == ')':
                if not stack or stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif item == ']':
                if not stack or stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            elif item == '}':
                if not stack or stack[-1] != '{':
                    return False
                else:
                    stack.pop()
        return not stack


if __name__ == '__main__':
    s = "()[]{"
    x = Solution()
    print(x.isValid(s))
