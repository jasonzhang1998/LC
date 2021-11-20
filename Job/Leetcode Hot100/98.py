# 验证二叉搜索树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 对树先进行一轮中序遍历
    # 然后判断中序遍历序列是不是单调递增的
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            seq.append(node.val)
            dfs(node.right)

        seq = []
        dfs(root)
        for i in range(1, len(seq)):
            if seq[i] <= seq[i - 1]:
                return False
        return True

    # 迭代版本的中序遍历写法
    def isValidBST2(self, root: TreeNode) -> bool:
        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.val <= inorder:
                return False
            inorder = root.val

            root = root.right

        return True

    # 递归版本，通过判断根节点是否在范围内，确定每个节点是否
    # 满足条件
    def isValidBST3(self, root: TreeNode) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.val

            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False

            if not helper(node.left, lower, val):
                return False

            return True

        return helper(root)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().isValidBST3(root))
