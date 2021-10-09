# 最长不含重复字符的子字符串


class Solution:
    # 动态规划思想，dp[i]表示以s[i]结尾的最长不重复子串
    # 状态转移可以通过维护一个不含重复元素的队列来完成
    # 队列的长度为子串的长度
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        # 初始元素入队，dp[0] = 1
        n = len(s)
        tmp = [s[0]]
        # dp数组可以优化，只用一个变量即可
        dp = [1] * n
        for i in range(1, n):
            # 如果新元素不在队列中，则新元素入队
            if s[i] not in tmp:
                tmp.append(s[i])
                dp[i] = len(tmp)
            else:
                # 如果发现新元素已经在队列中，即遇到重复元素
                # 此时队列元素开始出队，直到遇到重复的元素，将其出队
                while tmp[0] != s[i]:
                    tmp.pop(0)
                tmp.pop(0)
                tmp.append(s[i])
                dp[i] = len(tmp)
        return max(dp)

    # 观察到遇到重复元素，更新最大长度时，需要遍历队列
    # 可以使用一个哈希表代替队列来获取更新所需的信息
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        ans = tmp = 1
        dic = {s[0]: 0}
        for i in range(1, n):
            # 哈希表里面存放字符对应的索引
            j = dic.get(s[i], -1)
            dic[s[i]] = i
            # 通过索引来判断tmp如何更新
            if i - j > tmp:
                tmp += 1
            else:
                tmp = i - j
            ans = max(ans, tmp)
        return ans


if __name__ == '__main__':
    s = 'dvdf'
    print(Solution().lengthOfLongestSubstring2(s))
