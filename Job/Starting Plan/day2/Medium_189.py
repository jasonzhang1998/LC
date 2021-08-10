# 旋转数组

# 新建一个数组，通过取余数来判断原列表移动之后的元素在新列表的位置
# 空间复杂度为O(n)
def rotate(nums, k):
    n = len(nums)
    ans = [0] * n
    for i in range(n):
        pos = (i + k) % n
        ans[pos] = nums[i]
    for i in range(n):
        nums[i] = ans[i]
    return None


# 使用一个长度为k的中间数组去存储中间值，空间复杂度为O(1)
def rotate2(nums, k):
    if k == 0:
        return None
    n = len(nums)
    tmp = nums[:k]
    for i in range(n):
        pos1 = (i + k) % n
        pos2 = i % k
        a = nums[pos1]
        nums[pos1] = tmp[pos2]
        tmp[pos2] = a
    return None


# 数组翻转
def rotate3(nums, k):
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k % len(nums) - 1)
    reverse(nums, k % len(nums), len(nums) - 1)


def reverse(nums, start, end):
    for i in range((end - start + 1) // 2):
        temp = nums[end - i]
        nums[end - i] = nums[start + i]
        nums[start + i] = temp
    return None


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    # reverse(nums, 0, 2)
    print(rotate2(nums, 8))
    print(nums)
