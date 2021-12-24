# 根据身高重建队列
from typing import List


class Solution:
    # 先排序，再插队
    # 按身高逆序排序，再按k值正序排序。
    # 然后再按k值插入队列里面
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        # people = sorted(people, key=lambda x: (-x[0], x[1]))
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)
        return res


if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(Solution().reconstructQueue(people))
