# 打家劫舍III


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 动态规划
    # 状态转移方程与打家劫舍一致，dp[i] = max(dp[i - 1], dp[i -2] + num)
    # 把原来数组形式的dp转移改变成了树形式的dp转移
    def rob(self, root: TreeNode) -> int:
        def sup(node):
            if not node:
                return 0, 0
            leftp, leftq = sup(node.left)
            rightp, rightq = sup(node.right)
            # leftq + rightq 等价于原来的dp[i - 1]
            # leftp + rightp 等价于原来的dp[i - 2]
            # node.val 等价于原来的num
            return leftq + rightq, max(leftp + rightp + node.val, leftq + rightq)

        _, ans = sup(root)
        return ans


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print(Solution().rob(root))
