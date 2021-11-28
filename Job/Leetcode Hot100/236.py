# 二叉树的最近公共祖先


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 自底向上地寻找两个节点的公共祖先
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 判断一个节点是不是另一个节点的祖先
        def isAncestor(node1, node2):
            if not node1:
                return False
            if node1 == node2:
                return True
            return isAncestor(node1.left, node2) or isAncestor(node1.right, node2)

        if not root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        if left:
            return left
        right = self.lowestCommonAncestor(root.right, p, q)
        if right:
            return right
        if isAncestor(root, p) and isAncestor(root, q):
            return root

    # 自底向上递归,dfs搜索。
    # 深搜去找p，q节点，如果没找到就返回空，如果找到了则根据最近公共祖先的定义返回节点
    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        # 左右子节点没找到，返回空
        if not left and not right:
            return
        # 在右子树不在左子树，返回右子树的返回值
        if not left:
            return right
        # 在右子树不在左子树，返回右子树的返回值
        if not right:
            return left
        # 左右子树都有，则返回此时它们的父节点的值
        return root

    # 使用哈希表存储每个节点的父节点，通过dfs遍历一遍树得到
    # 然后从p节点开始，不断向上寻找父节点，将父节点路径存储到一visited数个组里面
    # 然后从q节点向上寻找父节点，遇到的第一个在visited数组里的节点则是最近公共祖先
    def lowestCommonAncestor3(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if node.left:
                dic[node.left] = node
                dfs(node.left)
            if node.right:
                dic[node.right] = node
                dfs(node.right)

        dic = {}
        dfs(root)
        visited = []
        while p:
            visited.append(p)
            if p in dic:
                p = dic[p]
            else:
                break
        while q:
            if q in visited:
                return q
            if q in dic:
                q = dic[q]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    node = Solution().lowestCommonAncestor3(root, root.left, root.right)
    print(node.val)
