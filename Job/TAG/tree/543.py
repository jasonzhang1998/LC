# 二叉树的直径

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left_dia, left_dep = dfs(node.left)
            right_dia, right_dep = dfs(node.right)

            return max(left_dia, right_dia, left_dep + right_dep), max(left_dep, right_dep) + 1

        return dfs(root)[0]

    def diameterOfBinaryTree2(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        self.ans = 0
        dfs(root)
        return self.ans
