# 二叉树的前序遍历


# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归写法
def preorderTraversal(root):
    def preorder(root):
        if not root:
            return
        ans.append(root.val)
        preorder(root.left)
        preorder(root.right)

    ans = list()
    preorder(root)
    return ans


# 迭代法进行遍历
def preorderTraversal2(root):
    res = []
    if not root:
        return res
    stack = []
    node = root
    while stack or node:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    print(preorderTraversal2(root))
