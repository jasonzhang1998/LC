# 连接后等于目标字符串的字符串对


from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    count += 1
        return count


if __name__ == '__main__':
    nums = ["123", "4", "12", "34"]
    print(Solution().numOfPairs(nums, '1234'))
