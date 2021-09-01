# 二叉树的最小深度


# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 深度优先搜索，递归求出子树的最小深度
def minDepth(root):
    if not root:
        return 0
    l = minDepth(root.left)
    r = minDepth(root.right)
    # 只有当左右子节点都不为空时，取其中小的
    # 否则取其中有效的深度
    if root.left and root.right:
        return min(l, r) + 1
    else:
        return max(l, r) + 1


# 广度优先搜索，将每一层的节点及其深度都入队出队，
# 当找到第一个叶子节点时，此时的叶子节点的深度为最小深度
def minDepth2(root):
    if not root:
        return 0
    queue = [(root, 1)]
    while queue:
        curSize = len(queue)
        for i in range(curSize):
            node, height = queue.pop(0)
            if not node.left and not node.right:
                return height
            if node.left:
                queue.append((node.left, height + 1))
            if node.right:
                queue.append((node.right, height + 1))


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    # root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    print(minDepth2(root))
