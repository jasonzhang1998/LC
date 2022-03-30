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


arr = [5, 2, 3, 4, 1, 3, 47, 8, 9]

partition(arr, 0, len(arr) - 1)
