# 重建二叉树
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归构建树，对于输入的preorder、inorder序列，每次递归需要做的就是
    # 构建根节点、求出左右子树的两个遍历序列，递归构造左右子树节点
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def resTree(pre_i: int, pre_j: int, in_i: int, in_j: int):
            if pre_j < pre_i or in_j < in_i:
                return
            if pre_j - pre_i == 0:
                root = TreeNode(preorder[pre_i])
                return root
            else:
                root = TreeNode(preorder[pre_i])
                left_len = 0
                right_len = 0
                full_len = pre_j - pre_i + 1
                for i in range(in_i, in_j + 1):
                    if inorder[i] == preorder[pre_i]:
                        left_len = i - in_i
                        right_len = full_len - left_len - 1
                        break
                root.left = resTree(pre_i + 1, pre_i + left_len, in_i, i - 1)
                root.right = resTree(pre_j - right_len + 1, pre_j, i + 1, in_j)
                return root

        n = len(preorder)
        return resTree(0, n - 1, 0, n - 1)

    # 利用哈希表来存放后续遍历序列里面值和索引的映射，
    # 这样就不用每次递归的时候都扫描一遍后序遍历序列
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def resTree(pre_i: int, pre_j: int, in_i: int, in_j: int):
            if pre_j < pre_i or in_j < in_i:
                return
            root = TreeNode(preorder[pre_i])
            left_len = 0
            right_len = 0
            full_len = pre_j - pre_i + 1
            # for i in range(in_i, in_j + 1):
            #     if inorder[i] == preorder[pre_i]:
            #         left_len = i - in_i
            #         right_len = full_len - left_len - 1
            #         break

            i = index[preorder[pre_i]]
            left_len = i - in_i
            right_len = full_len - left_len - 1

            root.left = resTree(pre_i + 1, pre_i + left_len, in_i, i - 1)
            root.right = resTree(pre_j - right_len + 1, pre_j, i + 1, in_j)
            return root

        n = len(preorder)
        index = {element: i for i, element in enumerate(inorder)}
        return resTree(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    x = Solution().buildTree2(preorder, inorder)
    print(x.val)
    print(x.left.val)
    print(x.right.val)
    print(x.right.left.val)
    print(x.right.right.val)
