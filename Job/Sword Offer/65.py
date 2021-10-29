# 不用加减乘除做加法


class Solution:
    # a^b得到非进位和，(a&b)<<1得到进位和
    # 循环计算进位和和非进位和，直到进位和为0，即没有进位
    def add(self, a: int, b: int) -> int:
        # python负数的特殊存储机制，需要特殊处理
        # 先求其补码，再加法计算，如果最后得到的结果是负数，则还需要还原
        x = 0xfffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), ((a & b) << 1) & x
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    print(Solution().add(2, 5))
