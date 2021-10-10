from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dic = {}
        ans = []
        nums2 = set(nums2)
        for num in nums1:
            dic[num] = 1
        for num in nums2:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] = 2
        for num in nums3:
            if num not in dic:
                continue
            else:
                dic[num] += 1
        for k, v in dic.items():
            if v > 1:
                ans.append(k)
        return ans


if __name__ == '__main__':
    nums1 = [1, 2, 2]
    nums2 = [4, 3, 3]
    nums3 = [5]
    print(Solution().twoOutOfThree(nums1, nums2, nums3))
