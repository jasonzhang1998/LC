
# input: list(int)
# length >= k

def getMinSum(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n
    # dp[i]表示以nums[i]结尾的最小子数组和的大小
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = min(dp[i - 1] + nums[i], nums[i])
    return min(dp)

def getMinSumK(nums, k):
    n = len(nums)
    if k >= n:
        return sum(nums)
    # dp[i]表示以nums[i]结尾的最小子数组和的大小
    dp = [0] * n
    dp[0] = nums[0]
    # dp[k - 1] = sum(nums[:k])
    for i in range(1, n):
        if i < k:
            dp[i] = min(dp[i - 1] + nums[i], nums[i])
            continue
        dp[i] = min(dp[i - k], 0) + sum(nums[i - k + 1:i + 1])
    return min(dp[k - 1:])



nums = [-18, 3, 4, -5, -1, 4]
# print(getMinSum(nums))
print(getMinSumK(nums, 6))

