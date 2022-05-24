# 对称二叉树

# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def issame(t1, t2):
            if not t1 and not t2:
                return True
            elif t1 and t2:
                if t1.val != t2.val:
                    return False
                return issame(t1.left, t2.right) and issame(t1.right, t2.left)
            else:
                return False
        if not root:
            return True
        return issame(root.left, root.right)

    # 基于层序遍历的迭代解法
    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True
        q1 = queue.deque()
        q2 = queue.deque()
        q1.append(root)
        q2.append(root)
        while q1 or q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if not node1 and not node2:
                continue
            if (not node1 or not node2) or node1.val != node2.val:
                return False
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.right)
            q2.append(node2.left)
        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(1)

print(Solution().isSymmetric2(root))
