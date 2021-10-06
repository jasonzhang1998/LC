# 1~n整数中1出现的次数


class Solution:
    # 分别计算每个位上1出现的次数
    def countDigitOne(self, n: int) -> int:
        ans = 0
        # 由于n的最大值位2^31,因此n最多为10位
        for i in range(10):
            cur = n // pow(10, i)

            # x 为该位上的数
            x = cur % 10
            # pre为该位之前的数的大小
            pre = n // pow(10, i + 1)
            # pos为该位之后数的大小
            pos = n % pow(10, i)

            if x == 0:
                count = pre * pow(10, i)
            elif x == 1:
                count = pre * pow(10, i) + pos + 1
            else:
                count = (pre + 1) * pow(10, i)
            ans += count
        return ans


if __name__ == '__main__':
    print(Solution().countDigitOne(3102))
