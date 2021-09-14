# 二进制中1的个数


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            x = n % 2
            if x == 1:
                count += 1
            n >>= 1
        return count


if __name__ == '__main__':
    n = 11
    print(Solution().hammingWeight(-1))
