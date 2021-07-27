import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split(" "))
arr = [[0] * (M + 1) for _ in range(N + 1)]  # N * M matrix
visited = [[0] * (M + 1) for _ in range(N + 1)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []

# 초기화
for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split(" "))
    for i in range(a, c):
        for j in range(b, d):
            arr[i][j] = 1
            visited[i][j] = 1


def dfs(x, y):
    cnt = 1
    visited[x][y] = 1
    stack = deque()
    stack.append([x, y])

    while stack:
        x, y = stack.pop()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < N and 0 <= new_y < M:
                if not visited[new_x][new_y]:
                    visited[new_x][new_y] = 1
                    stack.append([new_x, new_y])
                    cnt += 1

    result.append(cnt)


for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)

result.sort()
print(len(result))
print(*result)
