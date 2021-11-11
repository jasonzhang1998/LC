# 最小覆盖子串
import collections


class Solution:
    # 滑动窗口
    # 通过哈希表来判断滑动窗内的子串是否包含足够的元素
    # 滑动窗右边界一直向右延申，知道遍历完整个s
    # 每当滑动窗满足要求时，右边界停止，左边界收缩，直到窗口最小
    # 然后右边界继续延申
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        # n表示所需元素的总数，用来判断滑动窗是否满足要求
        n = len(t)
        if n > m:
            return ""

        # dic用于记录滑动窗内还需得到的元素的种类和对应个数
        dic = collections.Counter(t)
        # res记录最小滑动窗的左右边界
        res = (0, float('inf'))
        # i记录滑动窗的左边界
        i = 0
        # j是滑动窗的右边界，需遍历一遍s
        for j, c in enumerate(s):
            # 右边界延申，更新对应的值
            if dic[c] > 0:
                n -= 1
            dic[c] -= 1

            # 此时滑动窗内的元素符合要求，右边界停止
            if n == 0:
                # 此时收缩左边界的值
                while True:
                    c = s[i]
                    if c in dic.keys():
                        # 不能再继续收缩的时候，跳出循环
                        if dic[c] == 0:
                            break
                        dic[c] += 1
                    i += 1
                # 记录此时滑动窗的最小值
                if j - i < res[1] - res[0]:
                    res = (i, j)

                # 左边界右移一位，让滑动窗元素不够，使右边界继续延申
                dic[s[i]] += 1
                n += 1
                i += 1

        # 通过res的右边界是否更新，来判断有没有找到符合条件的滑动窗
        return "" if res[1] > m else s[res[0]: res[1] + 1]


if __name__ == '__main__':
    s = "cabwefgewcwaefgcf"
    t = "cae"
    print(Solution().minWindow(s, t))
