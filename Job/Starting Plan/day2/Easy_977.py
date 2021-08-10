# 有序数组的平方

# 直接平方之后排序，时间复杂度O(nlog(n))，空间复杂度O(log(n)),需要log(n)的栈空间用于排序
def sortedSquares(nums):
    return sorted(num * num for num in nums)


# 利用原数组有序的特点，使用双指针分别从头和尾开始比较，首指针指向的数平方更大，
# 则首指针后移一位，否则尾指针后移移位。同时将两个中更大的数从后往前赋值给答案数组
def sortedSquares2(nums):
    n = len(nums)
    ans = [0] * n
    i = 0
    j = n - 1
    for k in range(n):
        if abs(nums[i]) > abs(nums[j]):
            ans[n - 1 - k] = nums[i] * nums[i]
            i += 1
        else:
            ans[n - 1 - k] = nums[j] * nums[j]
            j -= 1
    return ans


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10]
    print(sortedSquares2(nums))
    print(abs(-3))
