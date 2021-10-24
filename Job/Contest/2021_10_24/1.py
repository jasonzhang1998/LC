# 句子中有效的单词数

class Solution:
    def countValidWords(self, sentence: str) -> int:
        chars = sentence.split()
        count = 0
        print(len(chars))
        for char in chars:
            flag = True
            x = 0
            for i in range(len(char)):
                if '0' <= char[i] <= '9':
                    flag = False
                    break
                elif char[i] in ['!', '.', ',']:
                    flag = (i == len(char) - 1)
                    if not flag:
                        break
                elif char[i] == '-':
                    if i == 0 or i == len(char) - 1:
                        flag = False
                        break
                    else:
                        pre = char[i - 1]
                        post = char[i + 1]
                        flag = 'a' <= pre <= 'z' and 'a' <= post <= 'z'
                        if not flag:
                            break
                    x += 1
            if flag and x <= 1:
                count += 1
        return count


if __name__ == '__main__':
    s = "q-o  x-p! g-l- q-n  f-o, m-u. m-i! y-k, i-j, d-p! e-t, h-u  j-j- d-z- v-w, r-a  i-h. d-a! z-o, v-l, "
    print(Solution().countValidWords(s))
    pass
