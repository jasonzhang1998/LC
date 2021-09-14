# 剪绳子
import math


class Solution:
    # 数学推导方法:
    # 根据算术几何均值不等式,可得,切分得到的绳段都想等时,乘积最大
    # 根据对绳段乘积函数求导,求极值,得到当尽可能以绳段长度为3进行切分时
    # 乘积最大  参考如下题解:
    # https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/mian-shi-ti-14-i-jian-sheng-zi-tan-xin-si-xiang-by/

    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        a = n // 3
        b = n % 3
        if b == 0:
            return int(math.pow(3, a))
        # 3 + 1需要变为 2 + 2
        elif b == 1:
            return int(math.pow(3, a - 1) * 4)
        else:
            return int(math.pow(3, a) * 2)

    # 贪心算法,将绳子尽可能多切分为长度为3的段,(也是建立在知道最优绳段为3的情况下)
    def cuttingRope2(selfself, n: int) -> int:
        if n < 4:
            return n - 1
        elif n == 4:
            return 4
        else:
            res = 1
            while n > 4:
                res *= 4
                n -= 3
        return res * n

    # 动态规划
    # dp[i]为长度为i的绳子剪碎之后的最大乘积
    # 对于长度为x的绳子,至少得剪一段,因此剪一段长度为j的绳子之后,
    # 剩下的绳子可以剪也可以不剪.如果不剪,则乘积为 j * (x - j)
    # 剪的话，则是j * dp[x - j]。
    # 通过枚举j的所有长度，找出乘积最大的剪法。
    def cuttingRope3(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            # 由于剪长度为1的绳子没有增益，因此j从2开始枚举到i - 2
            for j in range(2, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]


if __name__ == '__main__':
    print(Solution().cuttingRope3(5))
