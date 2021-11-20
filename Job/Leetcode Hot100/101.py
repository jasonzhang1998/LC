# 对称二叉树


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 根据对称树的节点对应关系，递归地判断每个对应节点值是否相等
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                return helper(node1.left, node2.right) and helper(node1.right, node2.left)

            return False

        return helper(root, root)

    # 迭代求法，每次入队两个对应的节点，出队时进行比较
    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = collections.deque()
        q.append(root)
        q.append(root)
        while q:
            node1 = q.popleft()
            node2 = q.popleft()

            if not node1 and not node2:
                continue
            if (not node1 or not node2) or node1.val != node2.val:
                return False

            q.append(node1.left)
            q.append(node2.right)

            q.append(node1.right)
            q.append(node2.left)
        return True


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.right = TreeNode(2)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(3)

    root = TreeNode(1)
    root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    # root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric2(root))
