# 相同的树


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    if (not p and q) or (not q and p):
        return False
    if not p and not q:
        return True
    # 根结点的值相同，并且左右子树也相同
    return q.val == p.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(1)
    p.right = TreeNode(2)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    print(isSameTree(p, q))
