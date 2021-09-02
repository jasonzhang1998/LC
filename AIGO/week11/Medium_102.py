# 二叉树的层序遍历


# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 使用一个列表queue来模拟队列，然后层序遍历二叉树
# 本质上是广度优先搜索
def levelOrder(root):
    if not root:
        return []
    queue = [root]
    ans = []
    while queue:
        tmp = []
        for i in range(len(queue)):
            node = queue.pop(0)
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(tmp)
    return ans


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    print(levelOrder(root))
