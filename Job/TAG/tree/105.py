# 从前序与中序遍历序列构造二叉树

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pstart, pend, istart, iend):
            if pstart > pend:
                return
            node = TreeNode(preorder[pstart])
            index = dic[node.val]
            left_length = index - istart
            node.left = build(pstart + 1, pstart + left_length, istart, index - 1)
            node.right = build(pstart + left_length + 1, pend, index + 1, iend)
            return node
        
        dic = {}
        n = len(preorder)
        for i in range(n):
            dic[inorder[i]] = i
        return build(0, n - 1, 0, n - 1)
