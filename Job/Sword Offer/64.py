# 求1+2+3+...+n

# 由于不能使用乘除法、if，switch、for、while等循环、判断语句
# 可以使用逻辑运算符实现函数是否运行，从而达到判断语句的效果
class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


if __name__ == '__main__':
    print(Solution().sumNums(100))
