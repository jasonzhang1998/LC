# 不同的二叉搜索树


class Solution:
    # 动态规划
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        # 求从1到n的不同二叉搜索树
        for i in range(1, n + 1):
            for j in range(i):
                # 状态转移方程
                # 累加以每个元素为根节点的不同二叉搜索树数量
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]


if __name__ == '__main__':
    print(Solution().numTrees(5))
