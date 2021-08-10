# 反转字符串中的单词


# 首先将字符串根据空格切分成列表，然后对每个字符串元素都转换成列表进行反转，
# 最后通过空格拼接起来
def reverseWords(s):
    list1 = s.split(' ')
    result = []
    for i in range(len(list1)):
        list2 = list(list1[i])
        list3 = reverse(list2)
        str1 = ''.join(list3)
        result.append(str1)
    return ' '.join(result)


# 辅助函数，用于反转字符列表，函数的输入和返回值都是列表类型
def reverse(s):
    n = len(s)
    for i in range(n // 2):
        temp = s[i]
        s[i] = s[n - 1 - i]
        s[n - 1 - i] = temp
    return s


# 利用字符串切片将字符串进行反转
def reverseWords2(s):
    return ' '.join([i[::-1] for i in s.split(' ')])


# 双指针法的辅助函数，用于反转给定区间的列表元素
def reverse2(list1, start, end):
    while start < end:
        list1[start], list1[end] = list1[end], list1[start]
        start += 1
        end -= 1


'''
双指针法翻转字符串，通过前后指针寻找字符串里的单词。
左右指针均从零开始，左指针先往后走，遇到非空格就停，
然后右指针从左指针的位置往后走，遇到空格就停，这样即找到了一个单词，
然后使用辅助函数将其翻转。翻转之后，左指针从右指针的位置开始往后走，重复上述操作，
直到左指针或右指针到达末尾
'''


def reverseWords3(s):
    n = len(s)
    i = j = 0
    list2 = list(s)
    while i < n and j < n:
        while i < n and list2[i] == ' ':
            i += 1
        j = i
        while j < n and list2[j] != ' ':
            j += 1
        reverse2(list2, i, j - 1)
        i = j
    return "".join(list2)


if __name__ == '__main__':
    s = "hello happy my god"
    # print(reverseWords2(s))
    s1 = 'wearefamily'
    # print(s1[::-1])
    print(reverseWords3(s))
