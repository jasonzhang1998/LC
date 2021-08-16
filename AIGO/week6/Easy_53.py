# 最大子序和


# 暴力搜索:i为起点，j为终点。每次计算一个子序列的和，取最大值
def maxSubArray(nums):
    n = len(nums)
    maxSum = nums[0]
    for i in range(n):
        curSum = 0
        for j in range(i, n):
            curSum += nums[j]
            if curSum > maxSum:
                maxSum = curSum
    return maxSum


# 贪心算法：将序列从头开始累加，每次累加如果当前和小于0，
# 则舍弃之前的序列，重新开始累加，如果当前和大于等于0，则继续累加，
# 记录每次累加的最大和
def maxSubArray2(nums):
    n = len(nums)
    curSum = 0
    maxSum = nums[0]
    for i in range(n):
        curSum += nums[i]
        if curSum > maxSum:
            maxSum = curSum
        if curSum < 0:
            curSum = 0
    return maxSum


# 动态规划：dp[i]表示以第i个元素结尾的连续子序列的最大和，因此dp数组中的最大值即为所求
# 状态转移为判断前一个状态的子序列最大和是否大于0，大于0则加入序列，小于0则重新开始
def maxSubArray3(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = nums[i] + max(0, dp[i - 1])
    return max(dp[i])


# 滚动数组实现动态规划
def maxSubArray4(nums):
    n = len(nums)
    pre = nums[0]
    cur = 0
    maxSum = nums[0]
    for i in range(1, n):
        cur = nums[i] + max(pre, 0)
        pre = cur
        if cur > maxSum:
            maxSum = cur
    return maxSum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray2(nums))
