# 路径总和III


# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 遍历 + dfs
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # dfs，求以某个节点为起点的和为num的路径有多少条
        def dfs(node, num):
            if not node:
                return 0

            res = 0
            # 这里找到之后不能直接返回
            # 而是路径加1，然后继续向下寻找
            if node.val == num:
                res += 1
            return dfs(node.left, num - node.val) + dfs(node.right, num - node.val) + res

        if not root:
            return 0
        # dfs， 遍历树的每个节点，累加以任一节点为起点
        left = self.pathSum(root.left, targetSum)
        right = self.pathSum(root.right, targetSum)
        return left + right + dfs(root, targetSum)

    # 前缀和
    def pathSum2(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(1)
    root.right = TreeNode(-3)
    root.right.right = TreeNode(11)
    print(Solution().pathSum2(root, 8))
