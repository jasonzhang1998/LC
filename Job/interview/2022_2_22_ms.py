def changeNum(nums):
    n = len(nums)
    left, right = 0, n - 1
    while left < right:
        while left < right and nums[right] % 2 == 0:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        while left < right and nums[left] % 2 == 1:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]
    return nums


if __name__ == '__main__':
    nums = [1, 3, 4, 6, 7, 8, 9]
    print(changeNum(nums))
