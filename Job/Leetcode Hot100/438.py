# 找到字符串中所有字母异位词
from typing import List


class Solution:
    # 滑动窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)
        return ans

    # 优化版滑动窗口
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(s[i]) - 97] += 1
            count[ord(p[i]) - 97] -= 1

        # differ用于记录当前窗口与p字符串中数量不同的字母的个数
        differ = [c != 0 for c in count].count(True)

        if differ == 0:
            ans.append(0)

        for i in range(s_len - p_len):
            # 某个字母数量由不同变为了相同
            if count[ord(s[i]) - 97] == 1:
                differ -= 1
            # 某个字母数量由相同变为了不同
            elif count[ord(s[i]) - 97] == 0:
                differ += 1
            count[ord(s[i]) - 97] -= 1

            # 某个字母数量由不同变为了相同
            if count[ord(s[i + p_len]) - 97] == -1:
                differ -= 1
            # 某个字母数量由相同变为了不同
            elif count[ord(s[i + p_len]) - 97] == 0:
                differ += 1
            count[ord(s[i + p_len]) - 97] += 1

            if differ == 0:
                ans.append(i + 1)
        return ans


if __name__ == '__main__':
    s = 'cbaebabacd'
    p = 'abc'
    print(Solution().findAnagrams2(s, p))
