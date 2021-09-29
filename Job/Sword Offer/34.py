# 二叉树中和为某一值的路径


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 通过回溯算法，穷举树的所有路径
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            return []

        # 回溯函数，用于
        def backtrack(root, target, path):
            # 递归结束条件
            # 当前结点为根结点，且target为0
            if not root.left and not root.right and target == 0:
                # 添加路径的时候不能直接添加path，这样是浅拷贝
                # 需要对path做一个切片，这样才是深拷贝
                res.append(path[:])
                return

            # 分别对左右子树进行递归
            if root.left:
                # 注意：这里是先添加到路径再调用回溯函数
                path.append(root.left.val)
                backtrack(root.left, target - root.left.val, path)
                # 回退操作
                path.pop()

            if root.right:
                path.append(root.right.val)
                backtrack(root.right, target - root.right.val, path)
                path.pop()

        res = []
        path = [root.val]
        backtrack(root, target - root.val, path)
        return res

    # 更加简洁优雅的代码实现
    def pathSum2(self, root: TreeNode, target: int) -> List[List[int]]:
        res, path = [], []

        def dfs(root, target):
            if not root:
                return
            path.append(root.val)
            target -= root.val

            if not root.left and not root.right and target == 0:
                res.append(path[:])

            dfs(root.left, target)
            dfs(root.right, target)
            path.pop()

        dfs(root, target)
        return res


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(Solution().pathSum2(root, 22))
