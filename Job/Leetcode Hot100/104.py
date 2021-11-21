# 二叉树的最大深度


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归地求树的深度
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

    # 层序遍历版本
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxDepth2(root))
