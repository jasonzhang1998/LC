# 路径总和


# Definition for a binary Tree Node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(hasPathSum(root, 3))
