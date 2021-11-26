# 多数元素
from typing import List


class Solution:
    # 投票算法
    def majorityElement(self, nums: List[int]) -> int:
        count = candidate = 0
        for x in nums:
            if count == 0:
                candidate = x
                count += 1
            else:
                if x == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate


if __name__ == '__main__':
    nums = [3, 2, 3]
    print(Solution().majorityElement(nums))
