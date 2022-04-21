# input

# n, k, x = map(int, input().split())
n, k, x = 4, 6, 16
maxNum = (k + k - n + 1) * n // 2
minNum = (1 + n) * n // 2
if n > k or x < minNum or x > maxNum:
    print(-1)
    exit()
sums = []
nums = [i for i in range(1, k + 1)]
cur = minNum
for i in range(n, k + 1):
    sums.append(cur)
    cur += n
i = 0
j = k - n
while i <= j:
    mid = (j - i) // 2 + i
    if sums[mid] == x:
        ans = nums[mid:n + mid + 1]
        out = ' '.join(map(str, ans))
        print(out)
        exit()
    elif sums[mid] < x:
        i = mid + 1
    else:
        j = mid - 1
ans = nums[j:n + j]
cur = sums[j]
index = n - (x - cur)
ans[index] = n + j + 1
# output
out = ' '.join(map(str, ans))
print(out)
