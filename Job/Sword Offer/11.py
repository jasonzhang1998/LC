# 旋转数组的最小数字
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        for i in range(len(numbers)):
            if i < len(numbers) - 1 and numbers[i + 1] < numbers[i]:
                return numbers[i + 1]
        return numbers[0]

    # 二分法的思想，最小值左侧的元素一定大于等于其右侧的元素
    def minArray2(self, numbers: List[int]) -> int:
        n = len(numbers)
        pre = 0
        pos = n - 1
        while pre < pos:
            mid = pre + (pos - pre) // 2
            # 此时说明最小值在右边
            if numbers[mid] > numbers[pos]:
                pre = mid + 1
            #     此时说明最小值在左边
            elif numbers[mid] < numbers[pos]:
                pos = mid
            else:
                # 相等的话，直接线性查找
                return min(numbers[pre:pos])
        return numbers[pre]


if __name__ == '__main__':
    numbers = [3, 3, 3, 5, 5, 5, 5, 8, 0, 1]
    print(Solution().minArray2(numbers))
