# 二叉树的镜像

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            # 将根结点的左右子树结点
            root.left, root.right = root.right, root.left
            # 分别对左子树和右子树进行交换
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
        return root


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    ans = Solution().mirrorTree(root)
    print(ans.right.left.val)
