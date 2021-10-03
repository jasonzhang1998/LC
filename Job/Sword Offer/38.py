# 字符串的排列
from typing import List


class Solution:
    # 通过依次与后面的元素交换来实现全排列
    def permutation(self, s: str) -> List[str]:
        def dfs(x):
            # 终止条件，长度到了n - 1，即遍历到了最后一位，此时不需要交换，直接返回
            if x == len(c) - 1:
                res.append("".join(c))
                return
            # c[x]在与之后的元素交换时，通过set来保证重复的元素只交换一次
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:
                    continue
                dic.add(c[i])
                # 与c[x]之后的每个元素都交换一次
                c[x], c[i] = c[i], c[x]
                dfs(x + 1)
                # 回溯操作，
                c[x], c[i] = c[i], c[x]

        if not s:
            return
        # 交换需要更改元素值，所以要把字符串的元素放进list
        c = []
        for i in s:
            c.append(i)
        res = []
        dfs(0)
        return res


if __name__ == '__main__':
    s = 'abb'
    print(Solution().permutation(s))
