class Solution:
    # 基于贪心的暴力模拟解法
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # 判断是否存在两个以上的非空堆
        def valid(items):
            count = 0
            for item in items:
                if item > 0:
                    count += 1
            if count > 1:
                return True
            return False
        
        # 最后的得分值
        score = 0
        # 使用数组来存放三个堆的石子数，便于排序取最大的连个堆
        items = [0] * 3
        items[0] = a
        items[1] = b
        items[2] = c
        # 取石子策略(贪心)，每次都取石子数最多的两个堆
        while valid(items):
            # 每次都对堆进行排序，确定三个堆按照石子数按升序排列
            items.sort()
            score += 1
            items[1] -= 1
            items[2] -= 1
        return score


if __name__ == "__main__":
    test = [[2, 4, 6], [4, 4, 6], [1, 8, 8]]
    for item in test:
        print(Solution().maximumScore(item[0], item[1], item[2]))
