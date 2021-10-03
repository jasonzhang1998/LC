from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        ans = [[0] * n for i in range(m)]
        for i in range(len(original)):
            ans[i // n][i % n] = original[i]
        return ans


if __name__ == '__main__':
    orig = [1, 2, 3, 4]
    print(Solution().construct2DArray(orig, 2, 2))
