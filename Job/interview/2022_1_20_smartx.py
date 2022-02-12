class RandomList:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyList(self, head):
        dic = {}
        node = head
        while head:
            dic[head] = RandomList(head.val)
            head = head.next

        for k, v in dic.items():
            v.next = dic.get(k.next)
            v.random = dic.get(k.random)
        return dic[node]


if __name__ == '__main__':
    print('hello')
    print('hello')
    print('hello')