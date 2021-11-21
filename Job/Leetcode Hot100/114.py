# 将二叉树展开为链表


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代写法，使用栈迭代地进行先序遍历
    # 使用inorder记录每个节点的前驱，然后修改前驱节点的左右孩子
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return root
        stack = [root]
        inorder = None
        while stack:
            node = stack.pop()
            if inorder:
                inorder.left = None
                inorder.right = node
            inorder = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # 递归法，保存右节点信息
    def flatten2(self, root: TreeNode) -> None:
        if not root:
            return
        self.flatten2(root.left)
        temp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        self.flatten2(temp)
        root.right = temp

    # 寻找前驱节点法
    def flatten3(self, root: TreeNode) -> None:
        cur = root
        while cur:
            if cur.left:
                temp = cur.right
                node = cur.left
                while node.right:
                    node = node.right
                node.right = temp
                cur.right = cur.left
                cur.left = None
            cur = cur.right


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    Solution().flatten3(root)
    print('done')
