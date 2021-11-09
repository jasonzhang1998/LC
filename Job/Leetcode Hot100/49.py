# 字母异位词分组
import collections
from typing import List


class Solution:
    # 利用哈希表判断是否是异位词，然后暴力搜索,超时了
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(word1, word2):
            dic = {}
            for c in word1:
                if c not in dic:
                    dic[c] = 1
                else:
                    dic[c] += 1
            for c in word2:
                if c not in dic:
                    return False
                else:
                    dic[c] -= 1
                    if dic[c] < 0:
                        return False
            return sum(dic.values()) == 0

        n = len(strs)
        ans = []
        flag = False
        for i in range(n):
            if not ans:
                ans.append([strs[i]])
                continue
            for j in range(len(ans)):
                if isAnagram(strs[i], ans[j][0]):
                    ans[j].append(strs[i])
                    flag = True
                    break
            if not flag:
                ans.append([strs[i]])
            flag = False

        return ans

    # 使用哈希表来存储分组的异位词
    # 哈希表的值就是异位词列表，键是能判断是否是异位词的标志
    # 标志可以是字符串排序之后的字符串，也可以是各个字母出现的频次
    # 这里实现记录频次的版本
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c) - ord('a')] += 1
            dic[tuple(count)].append(st)
        return list(dic.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams2(strs))
