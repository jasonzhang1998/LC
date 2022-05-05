# 字符串的总引力

class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        # total[i]表示以s[i]为结尾的子串的总引力值
        total = [1] * n
        dic = {}
        dic[s[0]] = 0
        for i in range(1, n):
            if s[i] not in dic:
                total[i] = total[i - 1] + i + 1
            else:
                total[i] = total[i - 1] + i - dic[s[i]]
            dic[s[i]] = i
        return sum(total)
