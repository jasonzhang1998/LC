# 填充每一个节点的下一个右侧节点指针II

# Definition for a Node.
import collections
from tkinter.messagebox import NO


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 基于队列的bfs层序遍历的解法
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        q = collections.deque()
        q.append(root)
        while q:
            pre = None
            for i in range(len(q)):
                node = q.popleft()
                if pre:
                    pre.next = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                pre = node
        return root

    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return
        start = root
        while start:
            dummy = Node()
            pre = dummy
            cur = start
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            start = dummy.next
        return root
