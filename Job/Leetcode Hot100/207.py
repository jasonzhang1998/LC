# 课程表
import collections
from typing import List


# prerequisites表示边，每个数表示图的节点，判断能否完成课程其实就等价于，
# 判断该图是不是有向无环图。
class Solution:
    # 使用拓扑排序的办法判断是否是有向无环图(BFS)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = collections.deque()

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)

        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses

    # DFS遍历，如果存在环，那么dfs必定会遍历到起点
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 返回False 从课程i为起点遍历的路径存在环
        # 返回True表示没有环
        def dfs(i):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False

            flags[i] = 1
            for adj in adjacency[i]:
                if not dfs(adj):
                    return False
            flags[i] = -1
            return True

        # flag为0表示未被访问过
        # flag为-1表示被从其它起点开始的dfs遍历过
        # flag为1表示被本次dfs遍历过
        flags = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]

        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


if __name__ == '__main__':
    grid = [[0, 1]]
    print(Solution().canFinish2(2, grid))
