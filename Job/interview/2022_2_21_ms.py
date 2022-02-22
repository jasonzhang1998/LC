import collections


def deleteCharacter(s):
    n = len(s)
    start, end = 0, 0
    pos = {}
    level = 0
    for i in range(n):
        if s[i] == '<':
            if level == 0:
                start = i
            level += 1
        if s[i] == '>':
            if level == 1:
                end = i
                pos[start] = end
            level -= 1
    new_s = ''
    start = 0
    for k, v in pos.items():
        new_s += s[start:k]
        start = v + 1
    new_s += s[start:]

    dic = collections.Counter(new_s)
    minCount = len(s)
    chars = []
    for v in dic.values():
        if v < minCount:
            minCount = v
    for k, v in dic.items():
        if v == minCount:
            chars.append(k)
    for ch in chars:
        strs = new_s.split(ch)
        new_s = ''
        for item in strs:
            new_s += item
    return new_s


if __name__ == '__main__':
    print(deleteCharacter('<ssd<s>d<>isda>aaab<csds>cddrrrd'))
