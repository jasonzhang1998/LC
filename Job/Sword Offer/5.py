# 替换空格


class Solution:
    def replaceSpace(self, s: str) -> str:
        n = len(s)
        ls = []
        for i in range(n):
            if s[i] == ' ':
                ls.append("%20")
            else:
                ls.append(s[i])
        ans = ''
        for i in range(n):
            ans += ls[i]
        return ans


if __name__ == '__main__':
    s = "i love you"
    print(Solution().replaceSpace(s))
