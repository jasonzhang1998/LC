# 实现五种排序方法


# 冒泡排序
# 从列表第一个元素开始，从前往后扫描，每次都将指针指向的元素与其他一个元素比较
# 若大于后一个元素,则与后一个元素交换,直到最大的元素到最后的位置
# 重复上述的冒泡过程n - 1躺,直到列表有序
def bubbleSort(alist):
    print("bubble sorting")
    for i in range(len(alist) - 1):  # 只需要进行n-1躺冒泡排序
        for j in range(len(alist) - 1 - i):  # 已经排好序的部分不用再比较
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    print(alist)
    return alist


# 选择排序
# 第i躺选择排序从第i个元素开始,从前往后扫描,如果发现有元素小于第i个元素,则与第i个元素交换
# 第i趟排序后,前i个元素有序,n-1躺排序之后,整个列表有序
def selectionSort(alist):
    n = len(alist)
    for i in range(n - 1):
        for j in range(i, n):
            # 每趟选择排序选择最小的值放到列表第i个位置
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]
    print(alist)
    return alist


# 插入排序
# 第i躺排序,选择第i+1个元素,在前i个元素中进行遍历(或折半查找),找到第i+1个元素的插入位置,
# 然后将插入位置之后的有序元素集体后移一位,n-1躺排序之后,整个列表有序
def insertionSort(alist):
    n = len(alist)
    # n-1躺排序
    for i in range(1, n):
        # 遍历的方式寻找插入位置
        # # 第i躺插入排序时,在前i个元素里找插入位置
        # for j in range(i):
        #     if alist[j] > alist[i]:
        #         temp = alist[i]
        #         # 移动元素时,得从最后一个元素开始移动(细节)
        #         for k in range(i - 1, j - 1, -1):
        #             alist[k + 1] = alist[k]
        #         alist[j] = temp
        #         break

        # 用折半查找来寻找插入位置
        left, right = 0, i
        mid = left + (right - left) // 2
        while left < right:
            if alist[mid] == alist[i]:
                break
            elif alist[mid] < alist[i]:
                left = mid + 1
            elif alist[mid] > alist[i]:
                right = mid
            mid = left + (right - left) // 2
        temp = alist[i]
        for k in range(i - 1, mid - 1, -1):
            alist[k + 1] = alist[k]
        alist[mid] = temp

    print(alist)
    return alist


# 快速排序
# 第一躺快速排序:选取第一个元素作为标的,low指针从0开始,high指针从n - 1开始,
# high先从后往前扫描,若指向的元素小于标的,则alist[low] = alist[high].然后high定住,
# low指针从前往后扫描,若指向的元素大于标的,则alist[high] = alist[low],然后low定住,
# high指针开始扫描,直到low == high,扫描结束.此时将标的赋值给low和high指针指向的值.
# 这样经过一趟排序之后,标的左边的数均小于标的,右边的数均大于等于标的.
# 之后再分别对分割后的两部分数进行快速排序

# 空间复杂度为O(log(n))的快速排序写法
# 为什么是这个空间复杂度,因为递归栈的深度为log(n),然后每次递归需要额外的空间平均为n
def quickSort2(alist):
    n = len(alist)
    if n <= 1:  # 递归终止条件
        return alist
    pivot = alist[0]  # 设置标的
    left = [alist[i] for i in range(1, n) if alist[i] < pivot]
    right = [alist[i] for i in range(1, n) if alist[i] >= pivot]
    return quickSort2(left) + [pivot] + quickSort2(right)


# 空间复杂度为O(log(n))的写法,全程在原列表alist上进行操作,只需用到递归栈
def quickSort(alist):
    # 首先假设划分算法已知,记为partition(),返回的是划分后的标的位置
    def quickSortHelper(alist, low, high):
        if low < high:
            pivotpos = partition(alist, low, high)
            quickSortHelper(alist, low, pivotpos - 1)
            quickSortHelper(alist, pivotpos + 1, high)

    def partition(alist, low, high):
        pivot = alist[low]  # 选取第一个元素为标的
        while low < high:
            while low < high and alist[high] >= pivot:
                high -= 1
            alist[low] = alist[high]
            while low < high and alist[low] <= pivot:
                low += 1
            alist[high] = alist[low]
        alist[low] = pivot
        return low

    quickSortHelper(alist, 0, len(alist) - 1)
    return alist


# 归并排序
# 递归的思想,先将列表递归地切分,然后从底层开始合并
def mergeSort(alist):
    # 用于合并的函数，输入是两个待合并列表，输出是合并后的列表
    def merge(left, right):
        res = []  # res用来存放合并后的结果
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res = res + left[i:] + right[j:]
        return res

    # 递归终止条件，当列表长度小于等于1时，不再切分
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    return merge(left, right)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 6, 78]
    # bubbleSort(alist)
    # selectionSort(alist)
    # insertionSort(alist)
    # print(quickSort(alist))
    print(mergeSort(alist))