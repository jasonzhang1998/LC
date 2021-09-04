# 只出现一次的数字
from functools import reduce
from typing import List


class Solution:
    # 将每个元素都异或一次，剩下的就是只出现一次的元素
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

    # 使用reduce累积函数进行计算
    # reduce(func, iterable),传入的参数为运算函数和可迭代对象
    def singleNumber2(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    nums = [2, 2, 3, 3, 4]
    x = Solution().singleNumber2(nums)
    print(x)
