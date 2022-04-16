from typing import List


class Solution:
    def longestGeometricSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        dic = {}
        for i in range(1, n):
            for j in range(i):
                temp = nums[i] / nums[j]
                if temp in dic:

                else:
                    dic[temp] = [2, i]
        print(dic)
        return max(dic.values()[0])


nums = [75, 81, 27, 25, 5, 9, 12, 1, 3, 1]
# nums = [3,6,9,12]
# nums = [2,4,8,16,32]
print(Solution().longestGeometricSeqLength(nums))
