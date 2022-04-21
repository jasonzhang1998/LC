# 最长上升等比数列长度

from typing import List
class Solution:
    def longestGeometricSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        # 这里一定要用生成式初始化，用*是浅拷贝
        dic = [{} for _ in range(n)]
        ans = 0
        for i in range(1, n):
            for j in range(i):
                temp = nums[i] / nums[j]
                if temp not in dic[j]:
                    dic[i][temp] = 2
                else:
                    dic[i][temp] = dic[j][temp] + 1
                ans = max(ans, dic[i][temp])
        return ans


nums = [75, 81, 27, 25, 5, 9, 12, 1, 3, 1]
# nums = [3,6,9,12]
# nums = [2,4,8,16,32]
print(Solution().longestGeometricSeqLength(nums))
