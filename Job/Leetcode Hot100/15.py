# 三数之和
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ans = []
        for i in range(n - 2):
            # 第一位去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            pre = i + 1
            pos = n - 1
            while pre < pos:
                tmp = nums[i] + nums[pre] + nums[pos]
                if tmp == 0:
                    ans.append([nums[i], nums[pre], nums[pos]])
                    # 第二位去重
                    while pre < n - 2 and nums[pre] == nums[pre + 1]:
                        pre += 1
                    pre += 1
                    pos -= 1
                elif tmp < 0:
                    pre += 1
                else:
                    pos -= 1
        return ans


if __name__ == '__main__':
    nums = [-2, 0, 0, 2, 2]
    print(Solution().threeSum(nums))
