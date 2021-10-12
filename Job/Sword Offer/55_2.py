# 平衡二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 自顶向下递归，先判断根节点是不是平衡，再递归地判断左右节点是不是平衡
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.height2(root.left)
        right = self.height2(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, node):
        if not node:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def height2(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            # 使用一个临时列表来存储每一层的节点
            # 实现分层的效果
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res

    # 自底向上递归，通过后序遍历的方式，先判断最底层的节点是不是平衡
    # 然后再判断其父节点是不是平衡，最后判断根节点是否平衡
    def isBalanced2(self, root: TreeNode) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            # 如果子树节点不平衡，或其子树深度差大于1，则该节点不平衡。返回-1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1

        return height(root) >= 0


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Solution().isBalanced2(root))
