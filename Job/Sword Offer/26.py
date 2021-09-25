# 树的子结构


# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 本题的精髓函数，判断两个树是不是匹配的函数
        # 两棵树从根节点开始比较，直到所有节点比较完，所有结点值都相等，则两棵树匹配
        def recur(t1, t2):
            if not t2:
                return True
            if not t1 or t1.val != t2.val:
                return False
            return recur(t1.left, t2.left) and recur(t1.right, t2.right)

        if A and B:
            # 以先序遍历的顺序判断A每颗子树是不是与B匹配
            return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
        else:
            return False


if __name__ == '__main__':
    A = TreeNode(3)
    A.left = TreeNode(4)
    A.right = TreeNode(5)
    A.left.left = TreeNode(1)
    A.left.right = TreeNode(2)
    B = TreeNode(4)
    B.left = TreeNode(1)
    print(Solution().isSubStructure(A, B))
