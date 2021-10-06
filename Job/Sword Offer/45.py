# 把数组排成最小的数
import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a = x + y
            b = y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)


if __name__ == '__main__':
    nums = ['123', '213']
    print(Solution().minNumber(nums))


    def comp(x, y):
        if x[1] > y[1]:
            return 1
        elif x[1] < y[1]:
            return -1
        else:
            return 0


    nums.sort(key=functools.cmp_to_key(comp))
    print(nums)
