# 最长递增子序列


# 动态规划
# dp[i]表示以第i个元素结尾的最大上升子序列的长度
# 状态转移是通过遍历之前的dp数组，找出能接在后面的最长子序列
def lengthOfLIS(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        maxNum = 1
        for j in range(i):
            # 寻找能接在后面的子序列，然后取一个最长的
            if nums[i] > nums[j] and dp[j] + 1 > maxNum:
                maxNum = dp[j] + 1
            dp[i] = maxNum
    return max(dp)


# 使用二分查找优化动态规划中取最长子序列的遍历过程
# 重新定义dp数组，dp[i]表示长度为i+1的上升子序列最小的末尾元素（即在等长的子序列中，选择末尾元素最小的子序列）
# 如何更新dp? 从头开始遍历nums数组，如果此时遍历到的数组值大于dp数组的最后一位元素，则直接将这个元素添加到dp
# 数组末尾。否则dp数组长度不变，对dp数组进行二分查找，修改某个dp数组的某个值，使得dp数组满足原有特性。
def lengthOfLIS2(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [nums[0]]
    for i in range(1, n):
        if nums[i] > dp[-1]:
            dp.append(nums[i])
        else:
            l = 0
            r = len(dp) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if dp[mid] == nums[i]:
                    break
                elif dp[mid] < nums[i]:
                    l = mid + 1
                elif dp[mid] > nums[i]:
                    r = mid - 1
            if dp[l] > nums[i]:
                dp[l] = nums[i]
        print(dp)
    return len(dp)


if __name__ == '__main__':
    nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
    print(lengthOfLIS2(nums))
