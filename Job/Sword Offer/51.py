# 数组中的逆序对

from typing import List


class Solution:
    # 暴力搜索O(n^2)，会超时
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    count += 1
        return count

    # 采用插入排序的思想，将原数组的元素有序地插入到列表tmp中
    # 由于tmp有序，因此可以用二分查找来寻找插入位置，如遇到相同元素
    # 则插入到相同元素的最后面，因此可以通过插入位置和tmp长度来判断
    # 其后面有多少个元素，即nums中，该元素之前有多少个大于改元素的数
    # 将所有元素都插入tmp，则遍历完成
    # 时间复杂度为O(nlog(n))
    def reversePairs2(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = []
        count = 0
        for i in range(n):
            if not tmp:
                tmp.append(nums[i])
                continue
            l = 0
            r = len(tmp)
            while l < r:
                mid = l + (r - l) // 2
                if tmp[mid] == nums[i]:
                    l = mid + 1
                elif tmp[mid] < nums[i]:
                    l = mid + 1
                else:
                    r = mid

            count += len(tmp) - l
            tmp.insert(l, nums[i])
        return count

    # 利用归并排序的思想计算逆序对
    # 首先将数组分成单个元素，然后进行合并
    # 合并的时候计算逆序对的数目
    def reversePairs3(self, nums: List[int]) -> int:
        def merge(l, r):
            if l >= r:
                return 0
            mid = l + (r - l) // 2
            res = merge(l, mid) + merge(mid + 1, r)
            i = l
            j = mid + 1
            pos = l
            # 开始合并
            while i <= mid and j <= r:
                # 左边的数组元素大，说明构成逆序对
                if nums[i] > nums[j]:
                    tmp[pos] = nums[j]
                    j += 1
                    # 逆序对数量为该元素及其之后的元素之和
                    res += mid + 1 - i
                else:
                    tmp[pos] = nums[i]
                    i += 1
                pos += 1
            # 合并完成后将剩余的尾巴加入辅助数组
            for k in range(i, mid + 1):
                tmp[pos] = nums[k]
                k += 1
                pos += 1
            for k in range(j, r + 1):
                tmp[pos] = nums[k]
                k += 1
                pos += 1
            # 修改原数组的值，变成有序的数组，避免之后重复计算
            nums[l: r + 1] = tmp[l: r + 1]
            return res

        tmp = [0] * len(nums)
        return merge(0, len(nums) - 1)


if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    print(Solution().reversePairs3(nums))
