# 复杂链表的复制

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # 先遍历一次，使用哈希表存放新建的节点，然后再遍历一次给指针赋值
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        return dic[head]


if __name__ == '__main__':
    head = Node(7)
    head.next = Node(13)
    # head.random = None
    head.next.next = Node(11)
    head.next.random = head
    head.next.next.next = Node(10)
    head.next.next.random = head.next.next.next
    head.next.next.next.next = Node(1)
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head

    x = Solution().copyRandomList(head)
