# 移动零


# 双指针法，左指针指向已处理序列的尾部，右指针指向待处理序列的头部。初始时都为0
# 如果右指针指向的值非零，则交换左右指针的值，左右指针均右移，否则只有右指针右移
def moveZeroes(nums):
    n = len(nums)
    l = r = 0
    while r < n:
        if nums[r] != 0:
            # temp = nums[r]
            # nums[r] = nums[l]
            # nums[l] = temp
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        r += 1

# 先遍历一遍数组，将不为零的元素赋值到数组前半部分，后半部分直接赋值为零
def moveZeroes2(nums):
    pos = 0
    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1
    while pos < len(nums):
        nums[pos] = 0
        pos += 1


if __name__ == '__main__':
    nums = [1, 2, 3, 0, 6, 8, 0, 9, 0]
    # nums = [0, 0, 1]
    moveZeroes2(nums)
    print(nums)
