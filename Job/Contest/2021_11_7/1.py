# 统计字符串中的元音子字符串

from collections import defaultdict
from typing import List


class Solution:
    # 暴力循环 时间复杂度：O(n^2)
    def countVowelSubstrings(self, word: str) -> int:
        chars = ['a', 'e', 'i', 'o', 'u']
        n = len(word)
        i = count = 0
        visited = set()
        # 枚举子字符串起点
        while i < n - 4:
            j = i
            visited.clear()
            # 从起点开始往后遍历，求出该起点开始的所有元音子字符串
            while j < n and word[j] in chars:
                visited.add(word[j])
                if len(visited) == 5:
                    count += 1
                j += 1
            i += 1
        return count

    # 滑动窗口  时间复杂度: O(n)
    def countVowelSubstrings2(self, word: str) -> int:
        ans = 0
        freq = defaultdict(int)
        for i, x in enumerate(word):
            if x in "aeiou":
                # 如果遇到辅音，则重置边界
                if not i or word[i - 1] not in "aeiou":
                    jj = j = i  # set anchor
                    freq.clear()
                freq[x] += 1

                # 找到了以word[i]结尾的元音字符串
                while len(freq) == 5 and all(freq.values()):
                    freq[word[j]] -= 1
                    j += 1

                # j - jj 表示以word[i]为结尾的元音子字符串数量
                ans += j - jj
        return ans


if __name__ == '__main__':
    word = 'cuaieuouac'
    # word = 'aeiouu'
    print(Solution().countVowelSubstrings2(word))
