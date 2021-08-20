# 乘积最大子数组


# 动态规划
# dp[i - 1][0]表示以第i个元素结尾的子数组乘积的最大值
# dp[i - 1][1]表示以第i个元素结尾的子数组乘积的最小值
# 对于当前元素nums[i]，如果它是正数，那么之前的最大值与它相乘之后，仍是最大值
# 如果它是负数，则原来的最大值变成了最小值，最小值可能就变成最大值
# 因此对于包含nums[i]元素的子数组乘积最大值，只与自身和之前子数组的最大值、最小值有关
def maxProduct(nums):
    if not nums:
        return None
    n = len(nums)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = nums[0]
    dp[0][1] = nums[0]
    for i in range(1, n):
        if nums[i] >= 0:
            dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i])
            dp[i][1] = min(dp[i - 1][1] * nums[i], nums[i])
        else:
            dp[i][0] = max(dp[i - 1][1] * nums[i], nums[i])
            dp[i][1] = min(dp[i - 1][0] * nums[i], nums[i])
    ans = [i[0] for i in dp]
    return max(ans)


# 考虑到原dp数组的状态只与前一个状态和当前值有关，因此可以用滚动数组
# 思想优化
def maxProduct2(nums):
    if not nums:
        return None
    n = len(nums)
    preMax = nums[0]
    preMin = nums[0]
    res = preMax
    for i in range(1, n):
        if nums[i] >= 0:
            curMax = max(preMax * nums[i], nums[i])
            curMin = min(preMin * nums[i], nums[i])
        else:
            curMax = max(preMin * nums[i], nums[i])
            curMin = min(preMax * nums[i], nums[i])
        res = max(res, curMax)
        preMax = curMax
        preMin = curMin
    return res


if __name__ == '__main__':
    nums = [2, 3, -2, 4, -3, 0]
    print(maxProduct2(nums))
