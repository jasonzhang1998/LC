# 恢复二叉搜索树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        nodes = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)
        
        dfs(root)
        i, j = 0, len(nodes) - 1
        while i < j:
            if nodes[i].val > nodes[i + 1].val:
                break
            i += 1
        while j > 0:
            if nodes[j].val < nodes[j - 1].val:
                break
                j -= 1
        temp = nodes[i].val
        nodes[i].val = nodes[j].val
        nodes[j].val = temp

