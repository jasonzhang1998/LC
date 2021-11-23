# 二叉树中的最大路径


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = float('-inf')

    # 递归地计算每个节点的最大贡献值
    def maxPathSum(self, root) -> int:
        def maxGain(node):
            # 空节点最大贡献值为0
            if not node:
                return 0
            # 自底向上计算最大贡献值
            leftGain = max(0, maxGain(node.left))
            rightGain = max(0, maxGain(node.right))

            # 每计算一个节点，就计算以该节点为根节点的树的最大路径和。
            # 使用self.ans来维护最大的路径和
            whole = node.val + leftGain + rightGain
            self.ans = max(self.ans, whole)

            # 每个节点的最大贡献值为其节点值，加上其左右子节点最大贡献值中较大的那个
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.ans


if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxPathSum(root))
