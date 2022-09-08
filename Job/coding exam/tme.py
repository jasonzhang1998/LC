from typing import List
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinCount(self, str: str) -> int:
        n = len(str)
        dic = collections.Counter(str)
        ans = 0
        # 记录去除原始字符串中的重复元素的操作次数
        for value in dic.values():
            ans += value // 2
        # 剩下的字符串如果超过26个字母，则每多一个就需要一次操作
        ans += max(0, n - ans - 26)
        return ans

    def getBinaryTrees(self , preOrder: List[int], inOrder: List[int]) -> List[TreeNode]:
        # write code here
        if not preOrder or not inOrder:
            return [None]
        ans = []
        for i in range(len(inOrder)):
            if inOrder[i] == preOrder[0]:
                # 所有的左右子树组合得到所有可能的树
                for left in self.getBinaryTrees(preOrder[1:i + 1], inOrder[:i]):
                    for right in self.getBinaryTrees(preOrder[i + 1:], inOrder[i + 1:]):
                        root = TreeNode(preOrder[0])
                        root.left = left
                        root.right = right
                        ans.append(root)
        return ans
    
    def getValueSum(self, tree: TreeNode) -> int:
        # 返回以node为根节点的新平衡数的最小权值和
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                self.ans += 1
                self.ans %= mod
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            # 如果不平衡，那么左右子树中权值较小的子树的权值需补充abs(left - right)
            # 每次总是假设该节点的权值为1，所以需加1
            self.ans += abs(left - right) + 1
            self.ans %= mod
            # 返回该节点的最小权值之和
            return left + right + abs(left - right) + 1

        mod = int(1e9 + 7)
        self.ans = 0
        dfs(tree)
        return self.ans

ans = Solution().getBinaryTrees([1,1,2], [1,2,1])
print(ans)
# for node in ans:
#     print(node.val)

print(Solution().getMinCount("abaab"))
root = TreeNode(0)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)
root.left.left.left = TreeNode(0)
root.left.left.right = TreeNode(0)
print(Solution().getValueSum(root))