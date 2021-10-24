# 下一个更大的数值平衡数

class Solution:
    # 暴力解法：遍历每一个比n大的数，直到找到第一个符合条件的数
    def nextBeautifulNumber(self, n: int) -> int:
        ans = n + 1
        while True:
            nums = []
            x = ans
            # 取出数x的每一位的数，放入nums里
            while x > 0:
                num = x % 10
                nums.append(num)
                x //= 10
            # 用哈希表统计每一位数出现的次数
            dic = {}
            for num in nums:
                if num not in dic:
                    dic[num] = 1
                else:
                    dic[num] += 1
            flag = True
            # 判断哈希表中所有数出现的次数是否等于它本身
            for key, value in dic.items():
                # 有一位不符合，则该数不是数值平衡数
                if key != value:
                    flag = False
                    break
            if flag:
                return ans
            else:
                ans += 1

    # 遍历该数各位数，使用一个数组来统计各个数字出现的次数
    def nextBeautifulNumber2(self, n: int) -> int:
        def isBalance(num):
            dic = [0] * 10
            while num > 0:
                i = num % 10
                dic[i] += 1
                num //= 10
            for i in range(10):
                if dic[i] > 0 and dic[i] != i:
                    return False
            return True

        x = n + 1
        while True:
            if isBalance(x):
                return x
            else:
                x += 1


if __name__ == '__main__':
    print(Solution().nextBeautifulNumber2(1000))
