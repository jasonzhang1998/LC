# 实现Trie(前缀树)


class Trie:

    def __init__(self):
        self.isEnd = False
        self.children = [None for _ in range(26)]

    def searchPrefix(self, prefix):
        node = self
        for item in prefix:
            index = ord(item) - ord('a')
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def insert(self, word: str) -> None:
        node = self
        for item in word:
            index = ord(item) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None
