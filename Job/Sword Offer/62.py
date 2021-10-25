# 圆圈中最后剩下的数字
import queue


class Solution:
    # 约瑟夫环，使用队列实现,会超时
    def lastRemaining(self, n: int, m: int) -> int:
        q = queue.Queue()
        for i in range(n):
            q.put(i)
        ans = 0
        while not q.empty():
            index = (m - 1) % q.qsize()
            for i in range(index):
                ans = q.get()
                q.put(ans)
            ans = q.get()
        return ans

    # 约瑟夫环的数学解法，设f(n)为n个数时候的解，则有如下递推关系：
    # f(n) = (f(n - 1) + m) % n
    # 具体推导过程参考
    # https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/jian-zhi-offer-62-yuan-quan-zhong-zui-ho-dcow/
    def lastRemaining2(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x


if __name__ == '__main__':
    print(Solution().lastRemaining2(51651, 3))
