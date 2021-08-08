# 二分查找
def search(nums, target):
    l = 0
    r = len(nums)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid
        elif nums[mid] < target:
            l = mid + 1
    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    print(search(nums, target))