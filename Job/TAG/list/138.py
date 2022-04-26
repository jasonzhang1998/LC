# 复制带随机指针的链表
import collections


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return

        dic = collections.defaultdict(Node)
        cur = head
        # 使用哈希表存放原节点和新节点的映射关系
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        # 遍历哈希表，建立新节点之间的映射关系
        # 需要注意，节点的next和random是否为空
        for k, v in dic.items():
            if k.next:
                v.next = dic[k.next]
            if k.random:
                v.random = dic[k.random]
        return dic[head]
