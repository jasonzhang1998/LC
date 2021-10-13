# 数组中数字出现的次数II
from typing import List


class Solution:
    # 将所有数都用二进制表示，对于每一个二进制位，统计所有数中这一位为1的数的个数
    # 如果个数能被3整除，说明要找的数这一位为0，否则为1
    # 这样即可求出要找的数的二进制表示，即找到了该数
    def singleNumber(self, nums: List[int]) -> int:
        k = max(nums)
        count = 0
        ans = 0
        while k > 0:
            tmp = 0
            for i in range(len(nums)):
                tmp += nums[i] % 2
                nums[i] >>= 1
            ans += (tmp % 3) * (2 ** count)
            k >>= 1
            count += 1
        return ans


if __name__ == '__main__':
    nums = [3, 4, 3, 3]
    print(Solution().singleNumber(nums))
