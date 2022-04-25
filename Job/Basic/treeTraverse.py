# 树的迭代版本的遍历方式

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 先序遍历
def preTraverse(root):
    results = []
    stack = []
    while root or stack:
        while root:
            results.append(root.val)
            stack.append(root)
            root = root.left
        node = stack.pop()
        if node.right:
            root = node.right
    return results


# 中序遍历
def midTraverse(root):
    results = []
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        results.append(node.val)
        if node.right:
            root = node.right
    return results


# 后序遍历，实际上是root->right->left遍历后的反转结果
def posTraverse(root):
    results = []
    stack = []
    while root or stack:
        while root:
            results.append(root.val)
            stack.append(root)
            root = root.right
        node = stack.pop()
        if node.left:
            root = node.left
    results.reverse()
    return results


tree1 = TreeNode(2)
tree1.left = TreeNode(1)
tree1.right = TreeNode(3)
tree1.right.left = TreeNode(4)
tree1.right.right = TreeNode(5)

print(posTraverse(tree1))
