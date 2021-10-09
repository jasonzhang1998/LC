# 第一个只出现一次的字符
import collections


class Solution:
    # 第一遍遍历，将各字符出现次数存入哈希表
    # 第二次遍历，找出第一个出现次数为1的字符
    def firstUniqChar(self, s: str) -> str:
        if not s or s == '':
            return ' '
        dic = collections.Counter(s)
        print(dic)
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return s[i]
        return ' '

    # 使用哈希表存放字符出现的次数是否为1
    # 遍历哈希表，键值第一个为True的key就是所求
    def firstUniqChar2(self, s: str) -> str:
        if not s or s == '':
            return ' '
        dic = dict()
        for c in s:
            dic[c] = not (c in dic)
        for k, v in dic.items():
            if v:
                return k
        return ' '


if __name__ == '__main__':
    s = 'sdhshff'
    print(Solution().firstUniqChar(s))
