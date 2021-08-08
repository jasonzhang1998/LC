# 搜索第一个错误的版本

def isBadVersion(num):
    return num % 2 == 0;

def search(n):
    l = 1
    r = n + 1
    while l < r:
        mid = l + (r - l) // 2
        if isBadVersion(mid):
            r = mid
        elif not isBadVersion(mid):
            l = mid + 1
    return l


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    print(search(nums, target))