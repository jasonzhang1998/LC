# 二叉树的最近公共祖先

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
            if node.val == q.val or node.val == p.val:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if not left and not right:
                return
            elif left and right:
                return node
            elif left:
                return left
            else:
                return right
        return dfs(root)

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dic = {}
        def dfs(node):
            if not node:
                return
            if node.left:
                dic[node.left] = node
            if node.right:
                dic[node.right] = node
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        visted = set()
        while p.val != root.val:
            visted.add(p)
            p = dic[p]
        while q.val != root.val:
            if q in visted:
                return q
            q = dic[q]
        return root

            
