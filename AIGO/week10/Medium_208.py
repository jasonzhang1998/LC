# 实现Trie(前缀树)


class Trie(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix):
        node = self
        for item in prefix:
            index = ord(item) - ord('a')
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def insert(self, word):
        node = self
        for item in word:
            index = ord(item) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.isEnd = True

    def search(self, word):
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix):
        return self.searchPrefix(prefix) is not None


example = Trie()
example.insert("sdsds")
