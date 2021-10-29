# 把字符串转换成整数


class Solution:
    def strToInt(self, str: str) -> int:
        if not str:
            return 0
        dic = {}
        s = '0123456789'
        for i in range(10):
            dic[s[i]] = i
        n = len(str)

        flag = True
        i = 0
        while i < n and str[i] == ' ':
            i += 1
        if i == n:
            return 0
        if str[i] in dic.keys():
            pass
        elif str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            flag = False
        else:
            return 0
        j = i
        while j < n and str[j] in dic.keys():
            j += 1
        if j == i:
            return 0
        ans = 0
        for k in range(i, j):
            ans *= 10
            ans += dic[str[k]]
        if not flag:
            ans = -ans
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        if ans > max_int:
            return max_int
        elif ans < min_int:
            return min_int
        else:
            return ans


if __name__ == '__main__':
    s = '-4359'
    print(Solution().strToInt(s))
