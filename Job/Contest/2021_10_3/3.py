# 石子游戏XI


from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = 0
        values = 0
        while stones and (values % 3 != 0 or values == 0):
            flag = 0
            print(values, count)
            print(stones)
            for stone in stones:
                if (values + stone) % 3 != 0:
                    stones.remove(stone)
                    values += stone
                    count += 1
                    flag = 1
                    break
            if flag == 0:
                values += stones[0]
                count += 1
        print(values, count)
        print(stones)
        if stones:
            return count % 2 == 0
        else:
            if values % 3 != 0:
                return False
            else:
                return count % 2 == 0


if __name__ == '__main__':
    stones = [1, 1, 7, 10, 8, 17, 10, 20, 2, 10]
    print(Solution().stoneGameIX(stones))
