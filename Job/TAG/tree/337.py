# 打家劫舍III

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            preleft, left = dfs(node.left)
            preright, right = dfs(node.right)
            return left + right, max(preleft + preright + node.val, left + right)
        return dfs(root)[1]
