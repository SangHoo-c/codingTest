import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split(" "))
arr = [[0] * (M+1) for _ in range(N+1)]     # N * M matrix
visited = [[0] * (M+1) for _ in range(N+1)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 초기화
for _ in range(K):
    a, b, x, y = map(int, sys.stdin.readline().split(" "))
    for i in range(a, x):
        for j in range(b, y):
            arr[i][j] = 1
            visited[i][j] = 1

result = []
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            queue = deque()
            queue.append([i, j])
            visited[i][j] = 1
            cnt = 1

            while queue:
                r, c = queue.popleft()

                for k in range(4):
                    new_r = r + dx[k]
                    new_c = c + dy[k]
                    if 0 <= new_r < N and 0 <= new_c < M:
                        if not visited[new_r][new_c]:
                            visited[new_r][new_c] = 1
                            queue.append([new_r, new_c])
                            cnt += 1
            result.append(cnt)

result.sort()
print(len(result))
print(*result)
