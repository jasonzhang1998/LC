# 二叉树的深度


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 后续遍历，递归实现
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return max(l, r) + 1

        return dfs(root)

    # 简洁版本的后续遍历
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth2(root.left), self.maxDepth2(root.right)) + 1

    # 层序遍历版本
    def maxDepth3(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            # 使用一个临时列表来存储每一层的节点
            # 实现分层的效果
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Solution().maxDepth3(root))
