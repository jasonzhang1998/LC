# 把二叉搜索树转换为累加树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                dfs(node.right)
                self.num += node.val
                node.val = self.num
                dfs(node.left)

        self.num = 0
        dfs(root)
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    x = Solution().convertBST(root)
    print(x)
