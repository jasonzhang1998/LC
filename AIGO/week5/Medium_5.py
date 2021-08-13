# 最长回文子串


# 动态规划解法，使用一个二维dp数组来表示状态，dp[i][j]状态表示的是
# s[i:j]是否是一个回文串。然后根据状态转移方程枚举所有子串是否是回文串
# 返回最长的回文子串
def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    dp = [[None] * n for _ in range(n)]
    # 单个字符肯定是回文串
    for i in range(n):
        dp[i][i] = True
    max_len = 1  # 记录回文子串的最大长度
    # 记录最长的回文子串的起始位置
    start = 0
    # 长度为2的子串，只需判断其两个元素是否相等
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2
            start = i
        else:
            dp[i][i + 1] = False
    for length in range(3, n + 1):  # 枚举子串时，从长度为3枚举到n
        for left in range(n - length + 1):  # 子串长度固定时，从头开始枚举
            right = left + length - 1
            if s[left] == s[right]:  # dp状态转移
                dp[left][right] = dp[left + 1][right - 1]
            else:
                dp[left][right] = False
            if dp[left][right] and right - left + 1 > max_len:  # 记录最长的子串长度，并更新最长的子串起始位置
                max_len = right - left + 1
                start = left
    return s[start:start + max_len]


# 中心拓展算法
# 从某个中心开始向两端延展，每延展一次判断是否是回文子串，记录此次延展的最长回文子串长度和起始位置
# 枚举所有的中心（n + n - 1个），取最长的回文子串
def longestPalindrome2(s):
    n = len(s)
    if n < 2:
        return s
    max_len = 1
    start = 0
    for mid in range(2 * n - 1):
        # 根据中心的位置，初始化拓展的起始位置
        if mid % 2 == 0:
            left = mid // 2 - 1
            right = mid // 2 + 1
        else:
            left = mid // 2
            right = mid // 2 + 1
        # 从中心开始向两端拓展
        while left >= 0 and right < n:
            if s[left] == s[right]:  # 两端字符相等则继续拓展
                left -= 1
                right += 1
            else:
                break
        # 若无法继续拓展，则说明此时的子串不是回文串，需要回退一步
        left += 1
        right -= 1
        # 记录最长的回文子串长度和起始位置
        if right - left + 1 > max_len and left >= 0 and right < n:
            max_len = right - left + 1
            start = left
    return s[start:start + max_len]


if __name__ == '__main__':
    s = "cbbd"
    print(longestPalindrome(s))
