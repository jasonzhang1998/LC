# 求x的平方根
# 牛顿迭代法或者二分法

# 二分法求平方根
def sqrtx(x):
    l = 1
    r = x
    mid = 0
    while l <= r:
        mid = l + (r - l) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            r = mid - 1
        elif mid * mid < x:
            l = mid + 1
    return r


# 牛顿迭代法，迭代20次
def sqrtx2(x):
    tmp = x / 2
    for i in range(20):
        tmp = (tmp + x / tmp) / 2
        print(tmp)
    return int(tmp)


# 牛顿迭代法，限定迭代误差
def sqrtx3(x):
    tmp = x / 2
    while (abs(tmp * tmp - x) > 1e-5):
        tmp = (tmp + x / tmp) / 2
        print(tmp)
    return int(tmp)


if __name__ == '__main__':
    x = 90
    print(sqrtx3(x))
