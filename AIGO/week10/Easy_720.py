# 词典中最长的单词


def longestWorld(words):
    valid = {""}
    for word in sorted(words, key=len):
        if word[0:-1] in valid:
            valid.add(word)
    return max(sorted(valid), key=len)


if __name__ == '__main__':
    words = ["ap", "apple", "a", "app"]
    print(longestWorld(words))
