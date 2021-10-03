# 找出缺失的观测数据


from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        n_sum = mean * (m + n) - sum(rolls)
        n_mean = n_sum / n
        ls = [1, 2, 3, 4, 5, 6]
        if n_mean > 6 or n_mean < 1:
            return []
        if n_mean in ls:
            return [int(n_mean)] * n
        base = int(n_mean)
        ans = [base] * n
        x = n_sum % n
        for i in range(x):
            ans[i] += 1
        return ans


if __name__ == '__main__':
    rolls = [1]
    print(Solution().missingRolls(rolls, 3, 1))
