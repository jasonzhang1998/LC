# 从上到下打印二叉树


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 使用队列实现bfs层序遍历
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop(0)
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder(root))
