# 比特位计数
from typing import List


class Solution:
    # nlog(n)的解法，计算每个数的二进制位上的1的数量
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            temp = i
            while temp > 0:
                ans[i] += temp % 2
                temp //= 2
        return ans

    # 线性时间复杂度解法
    # 分奇偶判断
    def countBits2(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            if i & 1 == 0:
                # 偶数，说明其二进制位最后一位为0
                # 因此其1的数目和其右移一位后的数的数目一样
                ans[i] = ans[i >> 1]
            else:
                # 奇数的话，比前面一位偶数多一个1
                ans[i] = ans[i - 1] + 1
        return ans


if __name__ == '__main__':
    print(Solution().countBits2(5))
