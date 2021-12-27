# 合并二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # dfs 递归地进行合并
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        def dfs(t1, t2):
            if not (t1 and t2):
                return t1 if t1 else t2

            t1.val += t2.val
            t1.left = dfs(t1.left, t2.left)
            t1.right = dfs(t2.right, t2.right)
            return t1

        return dfs(root1, root2)


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.left.left = TreeNode(5)
    root1.right = TreeNode(2)
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.left.right = TreeNode(4)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(7)

    x = Solution().mergeTrees(root1, root2)
