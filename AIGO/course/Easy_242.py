# 有效的字母异位词


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for item in s:
            if item in hash:
                hash[item] += 1
            else:
                hash[item] = 1
        for item in t:
            if item not in hash:
                return False
            else:
                hash[item] -= 1
        for item in hash:
            if hash[item] != 0:
                return False
        return True


if __name__ == '__main__':
    s = "ab"
    t = "a"
    print(Solution().isAnagram(s, t))
