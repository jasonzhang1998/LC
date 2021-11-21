# 从前序与中序遍历序列构造二叉树


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归地构造每个节点
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def construct(pleft, pright, ileft, iright):
            if pleft > pright:
                return
            node = TreeNode(preorder[pleft])
            index = dic[preorder[pleft]]
            length = index - ileft
            node.left = construct(pleft + 1, pleft + length, ileft, index - 1)
            node.right = construct(pleft + length + 1, pright, index + 1, iright)
            return node

        dic = {}
        n = len(preorder)
        for i in range(n):
            dic[inorder[i]] = i
        return construct(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = Solution().buildTree(preorder, inorder)
    print('done')
