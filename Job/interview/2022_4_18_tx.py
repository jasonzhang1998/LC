# def maxValue(matrix):
#     if not matrix:
#         return 0
#     m, n = len(matrix), len(matrix[0])
#     dp = [[0] * n for _ in range(m)]
#     dp[0][0] = matrix[0][0]
#     for i in range(m):
#         for j in range(n):
#             if i == 0 and j == 0:
#                 continue
#             elif i == 0:
#                 dp[i][j] = dp[i][j - 1] + matrix[i][j]
#             elif j == 0:
#                 dp[i][j] = dp[i - 1][j] + matrix[i][j]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
#     return dp[-1][-1]
#
#
# matrix = [[1, 2, 3],
#           [2, 4, 9]]
#
# print(maxValue(matrix))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSearchTree(root):
    # def dfs(node):
    #     if not node:
    #         return -float('inf'), float('inf')
    #     leftmax, leftmin = dfs(node.left)
    #     rightmax, rightmin = dfs(node.right)
    #     return max(node.val, leftmax, rightmax), min(node.val, leftmin, rightmin)
    #
    # if not root:
    #     return True
    # rightmax, rightmin = dfs(root.right)
    # leftmax, leftmin = dfs(root.left)
    # if leftmax < root.val < rightmin:
    #     return isSearchTree(root.left) and isSearchTree(root.right)
    # else:
    #     return False

    def dfs(node, up=float('inf'), down=-float('inf')):
        if not node:
            return True
        if node.val <= down or node.val >= up:
            return False

        return dfs(node.left, up=node.val, down=down) and dfs(node.right, down=node.val, up=up)

    return dfs(root)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

print(isSearchTree(root))

