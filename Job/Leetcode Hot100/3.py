# 无重复字符的最长子串


class Solution:
    # 使用哈希表维护已出现元素的最新索引，使用dp数组记录已某个元素为结尾的不重复字符串的长度
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dic = {}
        dp = [1] * n
        for i in range(n):
            if i == 0:
                dic[s[i]] = i
                dp[i] = 1
            else:
                # 如果之前没出现过，那么字符串长度直接加一
                if s[i] not in dic:
                    dp[i] = dp[i - 1] + 1
                else:
                    # 如果出现过，那么需要判断此字符和之前此字符之间有无重复元素
                    # 如果没有，则是索引之差，有则与前一位的字符串长度有关
                    # 得取他们之间的最小值
                    dp[i] = min(i - dic[s[i]], dp[i - 1] + 1)
                dic[s[i]] = i
        return max(dp)

    # 使用一个变量来优化dp数组
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        ans = tmp = 1
        dic = {s[0]: 0}
        for i in range(1, n):
            if s[i] not in dic:
                tmp += 1
            else:
                tmp = min(tmp + 1, i - dic[s[i]])
            dic[s[i]] = i
            ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    s = 'pwwkew'
    print(Solution().lengthOfLongestSubstring2(s))
