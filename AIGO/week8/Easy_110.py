# 平衡二叉树


# Definition for a binary Tree Node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    # 辅助函数用于求树的高度
    def heightOfTree(root):
        if not root:
            return 0
        left = heightOfTree(root.left)
        right = heightOfTree(root.right)
        return max(left, right) + 1

    if not root:
        return True
    else:
        boolean = abs(heightOfTree(root.left) - heightOfTree(root.right)) < 2
        # 根节点是平衡的，并且左右子树均是平衡的
        return boolean and isBalanced(root.left) and isBalanced(root.right)


def isBalanced2(root):
    # 求树的高度，同时判断当前树是不是平衡的
    def heightOfTree(root):
        if not root:
            return 0
        left = heightOfTree(root.left)
        right = heightOfTree(root.right)
        # 如果当前结点的左右子树不平衡，或者当前结点不平衡，则此树不平衡，返回-1
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        # 如果是平衡的，则返回当前树的高度
        return max(left, right) + 1

    return heightOfTree(root) >= 0


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    print(isBalanced2(root))
