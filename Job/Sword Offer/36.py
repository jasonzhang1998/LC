# 二叉搜索树与双向链表


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 已有一个二叉搜索树，要将其变为循环链表
    # 可以将树节点的left指针视为pre，right指针设为next
    # 本题实际考虑的就是通过修改每个节点的左右指针，使其成为一个有序的双向链表
    def treeToDoublyList(self, root: Node) -> Node:
        # dfs是一个中序遍历函数，以左根右的顺序遍历树
        # 这样即可以实现从小到大遍历树节点
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            # 每遍历到一个节点，则修改这个节点cur和其前驱pre之间的指针关系
            if self.pre:
                # 由于pre需要是全局变量，因此前面得加上self修饰
                self.pre.right, cur.left = cur, self.pre
            else:
                # 遍历第一个节点时不需要修改指针，只需记录它是头结点
                self.head = cur
            # 修改指针之后，pre后移，进入下一个节点
            self.pre = cur
            dfs(cur.right)

        if not root:
            return
        self.pre = None
        # 中序遍历完成之后，修改了n-1次指针关系，只剩下首尾节点之间的指针关系未修改
        dfs(root)
        # 将首尾节点指针修改，形成循环链表
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.right = Node(3)
    root.left.left = Node(1)

    x = Solution().treeToDoublyList(root)
    print(x.left.val)
    print(x.right.val)
