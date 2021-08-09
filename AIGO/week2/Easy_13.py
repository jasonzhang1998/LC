# 罗马数字转整数
def trans(s):
    n = len(s)
    hash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(1, n):
        if hash[s[i-1]] < hash[s[i]]:
            ans -= hash[s[i-1]]
        else:
            ans += hash[s[i-1]]
    ans += hash[s[n-1]]
    return ans


if __name__ == '__main__':
    str = "IIV"
    print(trans(str))
