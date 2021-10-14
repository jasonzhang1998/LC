# 翻转单词顺序


class Solution:
    # 使用split函数进行分割，然后列表reverse，最后拼接
    def reverseWords(self, s: str) -> str:
        res = s.split()
        res.reverse()
        return ' '.join(res)

    # 遍历字符串，取出遇到的单词，存入列表，最后倒序拼接返回
    def reverseWords2(self, s: str) -> str:
        n = len(s)
        word = ''
        res = []
        for i in range(n):
            # 如果遇到非空格，则此字母与当前单词拼接
            if s[i] != ' ':
                word += s[i]
                # 如果到达末尾，需将当前单词存入列表
                if i == n - 1:
                    res.append(word)
            else:
                # 如果遇到空格，通过单词是否为空来判断应该跳过还是应该把单词存入列表
                if not word:
                    continue
                else:
                    res.append(word)
                    word = ''
        res.reverse()
        return ' '.join(res)


if __name__ == '__main__':
    s = '    I  am  a student.'
    print(Solution().reverseWords2(s))
