# 二叉搜索树的第k大节点


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 中序遍历一遍，然后找出中序遍历序列的倒数第k个节点
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def midTraverse(node):
            if not node:
                return
            midTraverse(node.left)
            res.append(node.val)
            midTraverse(node.right)

        res = []
        midTraverse(root)
        n = len(res)
        return res[n - k]

    # 采用右根左顺序遍历，得到从大到小的遍历序列
    # 通过对self.k进行减操作来标记当前是第几个节点
    def kthLargest2(self, root: TreeNode, k: int) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            # 提前返回，如果self.k已经为0，则说明已找到元素，则直接返回
            if self.k == 0:
                return
            # 遍历到一个元素，就将self.k减一
            self.k -= 1
            # 遍历到第k个元素时，将节点值保存到结果中
            if self.k == 0:
                self.res = node.val
            dfs(node.left)

        self.k = k
        dfs(root)
        return self.res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Solution().kthLargest2(root, 1))
