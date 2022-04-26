# 填充每个节点的下一个右侧节点指针
# 给定的树是一个普通二叉树
import queue


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 最普通的使用队列进行bfs层序遍历
    def connect(self, root: Node) -> Node:
        if not root:
            return
        q = queue.deque()
        q.append(root)
        while q:
            pre = None
            for _ in range(len(q)):
                node = q.popleft()
                if pre:
                    pre.next = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                pre = node
        return root

    # 使用链表代替队列进行每一层的有序遍历
    def connect2(self, root: Node) -> Node:
        if not root:
            return
        start = root
        # start为每层链表的头节点
        while start:
            cur = start
            # dummy为下一层链表的虚拟头节点
            dummy = Node()
            pre = dummy
            # 遍历本层节点的过程中，建立下一层链表
            # 按顺序连接到dummy的后面
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            # 从下一层链表的dummy处获取下一层链表的头节点
            start = dummy.next
        return root
