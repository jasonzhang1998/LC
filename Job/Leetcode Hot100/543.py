# 二叉树的直径


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 自底向上计算每个节点的左右子树的深度
        # 每经过一个节点就计算以该节点为起点经过的最大的节点数目
        # 并更新此时最长的路径的节点数目
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) + 1

        # self.ans表示以某节点为起点经过的最多的节点的数量
        self.ans = 1
        depth(root)
        # 直径长度为经过的最大节点数减一
        return self.ans - 1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    print(Solution().diameterOfBinaryTree(root))
