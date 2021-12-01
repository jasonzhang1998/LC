# 二叉树的序列化与反序列化


# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # 将树编码为层序遍历序列，需编码空节点
    def serialize(self, root):
        if not root:
            return '[]'

        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('null')
        return '[' + ' '.join(res) + ']'

    #
    def deserialize(self, data):
        if data == '[]':
            return
        seq = data[1:-1].split(' ')
        queue = collections.deque()
        root = TreeNode(int(seq[0]))
        queue.append(root)
        i = 1
        while queue:
            node = queue.popleft()
            if seq[i] != 'null':
                node.left = TreeNode(int(seq[i]))
                queue.append(node.left)
            i += 1
            if seq[i] != 'null':
                node.right = TreeNode(int(seq[i]))
                queue.append(node.right)
            i += 1
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    x = Codec()
    s = x.serialize(root)
    y = x.deserialize(s)
    print(s)
    print(y)
