# 两数之和IV -输入BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(root):
            if not root:
                return False
            if root.val in dic:
                return True
            dic.add(k - root.val)
            return dfs(root.left) or dfs(root.right)
            
        dic = set()
        return dfs(root)
