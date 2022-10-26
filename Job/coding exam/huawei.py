# n = input()
# nums = list(map(int, input().split()))
class Solution:
    def solution(self, n, nums):
        def dfs(index, path):
            if index == n:
                if path[0] > path[1] > path[2]:
                    if path[0] - path[2] < self.distance:
                        self.distance = path[0] - path[2]
                        self.ans = path[:]
                        # print(self.ans)
                return
            res = total - sum(path)
            if path[1] - path[0] >= res or path[2] - path[0] >= res or path[2] - path[1] >= res:
                return
            for i in range(3):
                path[i] += nums[index]
                if (path[0], path[1], path[2], total - sum(path)) not in self.se:
                    self.se.add((path[0], path[1], path[2], total - sum(path)))
                    dfs(index + 1, path)
                path[i] -= nums[index]
        self.ans = []
        self.distance = float('inf')
        self.se = set()
        total = sum(nums)
        dfs(0, [0,0,0])
        return self.ans




print(Solution().solution(15, [105,589,458,296,23,5,6,7,8,9,10,12,34,5,56]))