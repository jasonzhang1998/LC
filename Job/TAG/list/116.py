# 填充每个节点的下一个右侧节点指针
# 给定的树是一个完美二叉树
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

    # 不使用队列，使用链表进行bfs
    def connect2(self, root: Node) -> Node:
        if not root:
            return
        head = root
        while head.left:
            cur = head
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            head = head.left
        return root

    # 对树进行dfs，遍历到每个节点时，让其左子树最右边的部分，和右子树最左边的部分相连
    def connect3(self, root: Node) -> Node:
        def dfs(root):
            if not root:
                return
            left = root.left
            right = root.right
            # left表示左子树最右边部分
            # right表示右子树最左边部分
            # 不断深入，让它们相连
            while left:
                left.next = right
                left = left.right
                right = right.left
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root
