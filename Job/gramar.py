import bisect
import collections


def partition(arr, left, right):
    if left >= right:
        return
    i, j = left, right
    while i < j:
        while i < j and arr[j] >= arr[left]:
            j -= 1
        while i < j and arr[i] <= arr[left]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    arr[i], arr[left] = arr[left], arr[i]
    return arr


arr = [5, 2, 3, 4, 1, 3, 47, 8, 4]

partition(arr, 0, len(arr) - 1)
print('hello')

nums = [1, 5, 9, 9, 9, 11, 13, 16]
k = collections.defaultdict(list)
index = bisect.bisect_left(nums, 10)
index1 = bisect.bisect_right(nums, 10)
print(index, index1)
