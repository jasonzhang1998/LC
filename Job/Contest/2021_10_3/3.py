# 石子游戏XI


from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # 因为只关心最后的和数是不是3的倍数，因此可以将所有的数对3取余
        s = [0, 0, 0]
        # 统计0， 1， 2各自出现的次数
        for i in stones:
            s[i % 3] += 1
        # 0的个数为偶数，即相当于没有0，次数bob无法靠拿0维持原有状态
        # 如果只有1或2，alice必输。反之alice可以通过若干对1，2将只有1或2的情况给bob，此时bob必输
        if s[0] % 2 == 0:
            return s[1] > 0 and s[2] > 0
        else:
            # 此时bob有一次可以维持原有状态的机会
            # 因此需要最后若干对1，2抵消后，剩下的1或2必须大于2，此时alice才能赢
            return abs(s[1] - s[2]) > 2


if __name__ == '__main__':
    stones = [1, 1, 7, 10, 8, 17, 10, 20, 2, 10]
    print(Solution().stoneGameIX(stones))
