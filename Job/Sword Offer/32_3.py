# 从上到下打印二叉树3


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 在分层打印的基础上，最后加一层循环，将奇数层反转
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        i, stack, res = 0, [root], []
        while stack:
            tmp = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(tmp)
        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        i = 0
        stack, res = [(root, i)], []
        while stack:
            node = stack.pop(0)
            if node[1] > len(res) - 1:
                res.append([])
            res[node[1]].append(node[0].val)
            if node[0].left:
                stack.append((node[0].left, node[1] + 1))
            if node[0].right:
                stack.append((node[0].right, node[1] + 1))
        for i in range(len(res)):
            if i % 2 == 1:
                res[i].reverse()
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().levelOrder2(root))
