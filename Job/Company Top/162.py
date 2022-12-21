from typing import List

class Solution:
    # 暴力遍历，时间复杂度O(n)
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i
        return n - 1
    
    # 二分搜索，时间复杂度O(log(n))
    def findPeakElement2(self, nums: List[int]) -> int:
        n = len(nums)
        # 处理数组越界情况，方便二分搜索
        def get(index):
            if index == -1 or index == n:
                return -float('inf')
            return nums[index]
        
        # 确定二分终止条件
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 如果是峰值，直接返回
            if get(mid) > get(mid - 1) and get(mid) > get(mid + 1):
                return mid
            # 如果比右边小，那么峰值肯定在右侧，否则肯定在左侧
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid
        


if __name__ == "__main__":
    test = [[1,2,3,1], [1,2,1,3,5,6,4]]
    for nums in test:
        print(Solution().findPeakElement2(nums))