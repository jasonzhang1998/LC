# 寻找两个正序数组的中位数
from typing import List


class Solution:
    # 先将两个数组归并，然后再取中位数
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        elif not nums1:
            tmp = nums2
        elif not nums2:
            tmp = nums1
        else:
            tmp = []
            p1 = p2 = 0
            while p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] <= nums2[p2]:
                    tmp.append(nums1[p1])
                    p1 += 1
                else:
                    tmp.append(nums2[p2])
                    p2 += 1
            while p1 < len(nums1):
                tmp.append(nums1[p1])
                p1 += 1
            while p2 < len(nums2):
                tmp.append(nums2[p2])
                p2 += 1
        n = len(tmp)
        if n % 2 == 0:
            return (tmp[n // 2] + tmp[n // 2 - 1]) / 2
        else:
            return tmp[n // 2]

    # 取两个数组的中位数，可以转换为取两个数组中的第k小的数
    # 通过二分查找，每次排除约k/2的元素
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            # index表示每次比较前，两个数组的头部元素的索引，初始时为0
            index1, index2 = 0, 0
            while True:
                # 数组nums1已经遍历完了，还没有找到
                if index1 == m:
                    # 此时第k大的元素就是数组nums2的第k小元素
                    return nums2[index2 + k - 1]
                if index2 == n:
                    # 数组nums2遍历完的情况
                    return nums1[index1 + k - 1]
                if k == 1:
                    # 第一小的元素就是两个数组头部元素中最小的那个
                    return min(nums1[index1], nums2[index2])

                # 计算新的待比较元素的索引，如果索引超过数组长度，那么直接设置为最尾部
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    # 排除了元素之后，k需变小，索引也需要更新
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLen = m + n
        if totalLen % 2 == 1:
            # 总长度为奇数，只需寻找一次
            return getKthElement((totalLen + 1) // 2)
        else:
            # 总长度为偶数，则需寻找两次，取平均
            return (getKthElement(totalLen // 2) + getKthElement(totalLen // 2 + 1)) / 2


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays2(nums1, nums2))
