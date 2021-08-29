# 从前序和中序遍历序列构造二叉树


# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    def myBuildTree(preLeft, preRight, inLeft, inRight):
        if preLeft > preRight:
            return None
        rootIndex = preLeft
        root = TreeNode(preorder[rootIndex])
        pIndex = hash[preorder[rootIndex]]
        leftNum = pIndex - inLeft
        root.left = myBuildTree(preLeft + 1, preLeft + leftNum, inLeft, pIndex - 1)
        root.right = myBuildTree(preLeft + leftNum + 1, preRight, pIndex + 1, inRight)
        return root

    hash = dict()
    n = len(inorder)
    for i in range(n):
        hash[inorder[i]] = i
    return myBuildTree(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    node = buildTree(preorder, inorder)
    print(node.right.right.val)
