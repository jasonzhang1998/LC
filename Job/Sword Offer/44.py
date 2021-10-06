# 数字序列中某一位的数字


class Solution:
    # 算法思想,先求出第n位数字所在的数是几位数
    # 然后找出该数在所有相同位数的数之间的相对位置
    # 之后找出该数,最后根据n找出是该数的第几位数字
    # 返回该数字
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        # 将各位数的最小下标存放到s中
        s = [0]
        # count初始为1,是因为得加上最初的0
        count = 1
        for i in range(1, 10):
            # 累加上所有i位数的位数总和
            count += i * 9 * pow(10, i - 1)
            s.append(count)
        # s = [0, 10, 190, 2890, 38890, 488890, 5888890, 68888890, 788888890, 8888888890]
        for i in range(len(s)):
            if s[i] > n:
                break

        # i为下标n所在的数的位数, index为n在所有该位数数字中的索引
        index_1 = n - s[i - 1]
        # k为n所在数字在所有该位数数字中的索引
        index_2 = index_1 // i
        # num为n所在的实际数字
        num = index_2 + pow(10, i - 1)
        # 下标n所代表的数字在num中的第pos位,pos为0,即代表最高位
        pos = index_1 % i

        # 求出n所在的位上的数
        pos = i - 1 - pos
        num = num // pow(10, pos)
        ans = num % 10
        return ans


if __name__ == '__main__':
    print(Solution().findNthDigit(185))
