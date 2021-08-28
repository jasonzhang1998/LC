# 二叉搜索树的最近公共祖先


# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root, p, q):
    maxVal = max(p.val, q.val)
    minVal = min(p.val, q.val)
    while root.val > maxVal or root.val < minVal:
        if root.val > maxVal:
            root = root.left
        elif root.val < minVal:
            root = root.right
    return root


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    print(lowestCommonAncestor(root, root.left.left, root.left.right).val)
