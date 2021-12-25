# 汉明距离


class Solution:
    # 先求出每个比特位，再用异或运算进行计数
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x > 0 or y > 0:
            count += (x & 1) ^ (y & 1)
            x >>= 1
            y >>= 1
        return count


if __name__ == '__main__':
    print(Solution().hammingDistance(1, 3))
