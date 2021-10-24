from collections import deque
from typing import List


# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.num = 1
        self.left = None
        self.right = None


class Solution:
    # 模拟建树的过程，会超时
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def dfs(tree):
            if not tree:
                return
            if tree.left:
                dfs(tree.left)
                tree.num += tree.left.num
            if tree.right:
                dfs(tree.right)
                tree.num += tree.right.num

        def dfs_value(n, tree):
            if not tree:
                return
            if tree.num == n:
                x = 1
            else:
                x = n - tree.num
            if tree.left:
                y = tree.left.num
            else:
                y = 1
            if tree.right:
                z = tree.right.num
            else:
                z = 1
            value = x * y * z
            res.append(value)
            dfs_value(n, tree.left)
            dfs_value(n, tree.right)

        n = len(parents)
        root = TreeNode(0)
        nodes = [root]
        res = []
        while nodes:
            node = nodes.pop(0)
            for j in range(1, n):
                if parents[j] == node.val:
                    node.left, node.right = node.right, node.left
                    node.left = TreeNode(j)
                    nodes.append(node.left)
        dfs(root)
        dfs_value(n, root)
        # print(res)
        max_value = max(res)
        ans = 0
        for num in res:
            if num == max_value:
                ans += 1
        return ans

    # 1、建树   2、dfs计算节点的num 和 value 3、遍历res寻找答案
    # 无需真正建立一棵树，通过四个变量分别记录树的val,num,left,right来表示一棵树
    # 本算法不会超时的关键在于建树的优化，无需用bfs建树，只需遍历一遍parents列表就能建树
    def countHighestScoreNodes2(self, parents: List[int]) -> int:
        # 递归计算每个节点的分数value
        def dfs(tree):
            # 此节点为空，直接返回
            if tree < 0:
                return

            # 计算每个节点的num，即以节点为根的树的节点个数
            left = dic[tree][2]
            right = dic[tree][3]
            # 根据左右根的遍历顺序，自底向上计算每个节点num
            if left > 0:
                dfs(left)
                dic[tree][1] += dic[left][1]
            if right > 0:
                dfs(right)
                dic[tree][1] += dic[right][1]

            # 自底向上计算节点的num之后，开始计算节点的value

            # 根节点特殊处理
            if dic[tree][1] == n:
                x = 1
            else:
                x = n - dic[tree][1]

            # 左子树为空的话，num就置为1
            if left > 0:
                y = dic[left][1]
            else:
                y = 1

            # 右子树为空的话，num就置为1
            if right > 0:
                z = dic[right][1]
            else:
                z = 1

            # value 的计算公式，计算完添加到节点分数列表里
            value = x * y * z
            res.append(value)

        dic = {}
        res = []
        n = len(parents)
        # 新建n个树节点
        for i in range(n):
            # dic[i] = [val, num, left, right]
            dic[i] = [i, 1, -1, -1]
        # 遍历parents列表，建立树节点之间的父子关系
        for i in range(1, n):
            fa = parents[i]
            if dic[fa][2] < 0:
                dic[fa][2] = i
            else:
                dic[fa][3] = i
        # 遍历整棵树，计算每个节点的分数value
        dfs(0)
        max_value = max(res)
        ans = 0

        # 遍历所有节点的分数，找出最高分数的节点数量，并返回
        for num in res:
            if num == max_value:
                ans += 1
        return ans


if __name__ == '__main__':
    nums = [-1, 2, 0, 2, 0]
    print(Solution().countHighestScoreNodes2(nums))
