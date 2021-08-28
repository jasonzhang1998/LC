# 二叉树的所有路径


# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binaryTreePath(root):
    def backtrack(node):
        track.append(str(node.val))
        if not node.left and not node.right:
            ans.append("->".join(track))
            return
        if node.left:
            backtrack(node.left)
            track.pop()
        if node.right:
            backtrack(node.right)
            track.pop()

    track = []
    ans = []
    backtrack(root)
    return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print(binaryTreePath(root))
