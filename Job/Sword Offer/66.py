# 构建乘积数组
from typing import List


class Solution:
    # 暴力计算，两层循环，会超时
    def constructArr(self, a: List[int]) -> List[int]:
        ans = []
        for i in range(len(a)):
            x = 1
            for j in range(len(a)):
                if j == i:
                    x *= 1
                else:
                    x *= a[j]
            ans.append(x)
        return ans

    # 使用两个dp数组分别正向、反向计算数组的前缀积
    def constructArr2(self, a: List[int]) -> List[int]:
        n = len(a)
        tmp1 = [1] * n
        tmp2 = [1] * n
        ans = [0] * n
        # 正向计算前缀积，tmp1[i]表示a[i]之前的元素的乘积
        for i in range(1, n):
            tmp1[i] = tmp1[i - 1] * a[i - 1]
        # 反向计算前缀积，tmp2[i]表示a[i]之后的元素的乘积
        for j in range(n - 2, -1, -1):
            tmp2[j] = tmp2[j + 1] * a[j + 1]
        # ans[i]为a[i]之前的元素乘积，乘以a[i]之后的元素的乘积
        for i in range(n):
            ans[i] = tmp1[i] * tmp2[i]
        return ans

    # 可以使用答案数组去存储正向的前缀积结果
    # 使用一个tmp变量去存储反向的前缀积结果，一边存储一边更新答案数组
    def constructArr3(self, a: List[int]) -> List[int]:
        n = len(a)
        tmp = 1
        ans = [1] * n
        for i in range(1, n):
            ans[i] = ans[i - 1] * a[i - 1]
        print(ans)
        for i in range(n - 2, -1, -1):
            tmp *= a[i + 1]
            ans[i] *= tmp
        return ans


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(Solution().constructArr3(a))
