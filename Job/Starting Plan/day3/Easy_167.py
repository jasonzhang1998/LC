# 两数之和2——输入有序数组


# 双指针，分别从数组头尾向中间进行扫描
def twoSum(numbers, target):
    n = len(numbers)
    left = 0
    right = n - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1


if __name__ == '__main__':
    numbers = [1, 3, 4, 7, 13, 45]
    print(twoSum(numbers, 14))
