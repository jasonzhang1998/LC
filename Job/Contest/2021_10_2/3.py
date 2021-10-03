# 考试的最大困扰度


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 滑动窗算法求最大连续的1
        def longestOne(nums, k):
            n = len(nums)
            ans = left = lsum = rsum = 0
            for right in range(n):
                rsum += nums[right]
                while lsum < rsum - k:
                    lsum += nums[left]
                    left += 1
                ans = max(ans, right - left + 1)
            return ans

        nums1 = []
        nums2 = []
        # 将T和F分别设为0，1或1，0，分别计算最大连续的T和F，然后取最大值
        for i in range(len(answerKey)):
            if answerKey[i] == 'T':
                nums1.append(0)
                nums2.append(1)
            else:
                nums1.append(1)
                nums2.append(0)
        print(nums1)
        print(nums2)
        return max(longestOne(nums1, k), longestOne(nums2, k))


if __name__ == '__main__':
    answerKey = 'TFFT'
    print(Solution().maxConsecutiveAnswers(answerKey, 1))
