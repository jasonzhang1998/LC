# 二叉树的中序遍历


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归写法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        ans = []
        dfs(root)
        return ans

    # 迭代写法
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal2(root))
