# 按位与结果大于零的最长组合
from typing import List

# 根据数据范围，这题肯定不能用dp
# 解法为统计所有数的各个二进制位上1的总数量
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = [0] * 30
        for num in candidates:
            i = 0
            while num > 0:
                res[i] += num & 1
                num >>= 1
                i += 1
        return max(res)
