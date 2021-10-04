# 数组中出现次数超过一半的数字
from typing import List


class Solution:
    # 暴力解法，使用哈希表存放每个元素的次数，最后返回次数最多的元素
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        # 将元素与对应的出现次数存入哈希表
        for i in range(n):
            if nums[i] in dic.keys():
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1

        ans = nums[0]
        # 遍历哈希表，返回出现次数最多的元素
        for key, value in dic.items():
            if value > dic[ans]:
                ans = key
        return ans

    # 先讲数组排序，由于该元素次数超多数组长度的一半，
    # 因此排序后数组的中间位置一定是该数
    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    # 投票算法
    # candidate表示候选的众数，count表示其出现次数
    # 遍历数组，遇到和candidate相同的数count加一，否则count减一
    # count归零之后，重新赋值candidate
    # 算法思想为,与candidate相同的元素越多,它的赞同声越大,反对声越小
    # 最后经过所有人投票,获得最高票的就是众数(因为数量不够的元素会被众数元素反对,从而下台)
    def majorityElement3(self, nums: List[int]) -> int:
        n = len(nums)
        candidate = count = 0
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
    print(Solution().majorityElement3(nums))
