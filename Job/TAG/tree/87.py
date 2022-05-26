# 扰乱字符串

import functools
from collections import *


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @functools.lru_cache(None)
        # dfs表示两端字符串是否和谐，即是否为扰乱字符串
        # 第一段字符串的起点为i1， 第二段字符串的起点为i2， 长度均为length
        def dfs(i1, i2, length):
            # 如果字符串相等则直接是和谐的
            if s1[i1: i1 + length] == s2[i2: i2 + length]:
                return True
            # 如果字符串中字符的种类和数目不一致，那肯定不是和谐的
            if Counter(s1[i1: i1 + length]) != Counter(s2[i2: i2 + length]):
                return False

            # 直接枚举所有分割长度，如果有一种解决方案是和谐的，则是和谐的
            for i in range(1, length):
                # 分割后不交换的情况，即s1前半段对应s2前半段，后半段对应后半段
                if dfs(i1, i2, i) and dfs(i1 + i, i2 + i, length - i):
                    return True
                # 分割后交换的情况，s1前半段对应s2后半段，后半段对应前半段
                if dfs(i1, i2 + length - i, i) and dfs(i1 + i, i2, length - i):
                    return True
            return False

        ans = dfs(0, 0, len(s1))
        dfs.cache_clear()
        return ans


print(Solution().isScramble('rgeat', 'great'))
