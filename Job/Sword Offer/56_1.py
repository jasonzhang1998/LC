# 数组中数字出现的次数
from typing import List


class Solution:
    # 将所有数字异或，得到结果tmp，因为只出现一次的两个数不同，所有tmp二进制位肯定有一位为1，并且这两个数这一位不同
    # 根据二进制位这一位是否为1，可以将所有元素分为2组，这两个数分别属于其中一组
    # 分别对两组的所有数进行异或，得到的结果就是要找的那两个数
    def singleNumbers(self, nums: List[int]) -> int:
        tmp = 0
        # 将所有数异或
        for num in nums:
            tmp ^= num
        print(tmp)
        dim = 1
        # 通过与操作找出为1的那个二进制位
        while dim & tmp != dim:
            dim <<= 1
        a = b = 0
        # 根据该二进制位是否为1，将元素分为两组，分别异或
        for num in nums:
            if num & dim == dim:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 3, 1, 2, 6]
    print(Solution().singleNumbers(nums))
