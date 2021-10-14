# 左旋转字符串


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        pre = s[:n]
        pos = s[n:]
        return pos + pre


if __name__ == '__main__':
    s = "lrloseumgh"
    print(Solution().reverseLeftWords(s, 6))
