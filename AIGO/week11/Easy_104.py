# 二叉树的最大深度


# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归求树的深度，相当于dfs
def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1


# 使用一个列表来模拟队列，采用层序遍历求树的最大深度
def maxDepth2(root):
    if not root:
        return 0
    queue = [root]
    height = 0
    while queue:
        # 求出这一层的节点数量
        curSize = len(queue)
        for i in range(curSize):
            # 将这一层的节点全部出队，然后将下一层的节点全部入队
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        # 每出队一层，高度加一
        height += 1
    return height


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(maxDepth2(root))
