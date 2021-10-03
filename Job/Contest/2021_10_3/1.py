from typing import List


class Solution:
    def minimumMoves(self, s: str) -> int:
        def numX(s):
            count = 0
            for i in range(n):
                if s[i] == 'x':
                    count += 1
            return count

        n = len(s)
        c = list(s)
        ans = 0
        while numX(c) != 0:
            for i in range(n):
                if c[i] == 'x' and i < n - 2:
                    c[i] = 'o'
                    c[i + 1] = 'o'
                    c[i + 2] = 'o'
                    break
                elif c[i] == 'x' and i == n - 2:
                    c[i] = 'o'
                    c[i + 1] = 'o'
                    break
                elif c[i] == 'x' and i == n - 1:
                    c[i] = 'o'
                    break
            ans += 1
        return ans


if __name__ == '__main__':
    s = 'xxoooo'
    print(Solution().minimumMoves(s))
