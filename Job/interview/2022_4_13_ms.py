# 升序数组nums

# shift：


def searchTarget(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    if target == nums[0]:
        return 0
    if target < nums[0]:
        flag = False
    while left <= right:
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        elif nums[mid] < nums[0]:
            if nums[mid] < target < nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[0] < target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 1, 2, 3]
    print(searchTarget(nums, 5))
