# 对称的二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 将树翻转的函数
        def mirrorTree(node: TreeNode) -> TreeNode:
            if not node:
                return None
            node.left, node.right = node.right, node.left
            mirrorTree(node.left)
            mirrorTree(node.right)
            return node

        # 判断两棵树是否相同
        def sameTree(t1, t2):
            if not t1 and not t2:
                return True
            elif t1 and t2:
                return t1.val == t2.val and sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)
            else:
                return False

        if not root:
            return True
        mirror = mirrorTree(root.left)
        # 一棵树对称，即左子树翻转之后与右子树相等
        return sameTree(mirror, root.right)


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    print(Solution().isSymmetric(root))
