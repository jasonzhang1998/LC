# 最接近的三数之和


# 由于数组原先无序，首先需要将数组排序，然后使用三指针进行扫描，找出最接近的数
# 其实去重操作可有可无，因为不会影响时间复杂度
def threeSumCloset(nums, target):
    n = len(nums)
    i = 0
    distance = 100000
    nums.sort()
    ans = 0
    while i < n - 2:
        # 如果当前枚举的数与前一个相同，则可以跳过这轮枚举，因为上一轮枚举的数的范围包含这轮枚举的范围
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        right = n - 1
        left = i + 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if abs(sum - target) < distance:
                distance = abs(sum - target)
                ans = sum
            if sum == target:
                return sum
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1
        i += 1
    return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 0]
    print(threeSumCloset(nums, 50))
