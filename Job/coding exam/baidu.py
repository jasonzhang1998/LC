import queue



def getMinSteps(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]
    q = queue.deque()
    q.append((0, 0))
    pos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    count = 0
    visited[0][0] = True
    while q:
        print(q)
        for i in range(len(q)):
            item = q.popleft()
            if item[0] == m - 1 and item[1] == n - 1:
                return count
            visited[item[0]][item[1]] = True
            for direc in pos:
                x, y = item[0] + direc[0], item[1] + direc[1]
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if matrix[item[0]][item[1]] == 'r':
                        if matrix[x][y] == 'r' or matrix[x][y] == 'e':
                            q.append((x, y))
                            visited[x][y] = True
                    if matrix[item[0]][item[1]] == 'e':
                        if matrix[x][y] == 'd' or matrix[x][y] == 'e':
                            q.append((x, y))
                            visited[x][y] = True
                    if matrix[item[0]][item[1]] == 'd':
                        if matrix[x][y] == 'r' or matrix[x][y] == 'd':
                            q.append((x, y))
                            visited[x][y] = True
        # print(count)
        count += 1
    return -1
            
    # return dfs(0, 0)


# m, n = map(int, input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(input()))
m, n = 3, 3
matrix = [['r', 'e', 'd'], ['d', 'e', 'r'], ['r', 'd', 'r']]

visited = set()

print(getMinSteps(matrix))
