"""
실행시간이 매우 오래걸린 코드 
refactoring 이 필요하다. 
"""

import sys
from collections import deque

# N 이 세로, M 이 가로 길이
M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
_queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            _queue.append([i, j, 0])
            visited[i][j] = 0

while _queue:
    r, c, cost = _queue.popleft()
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]

        if 0 <= x < N and 0 <= y < M:
            if arr[x][y] == 0 and visited[x][y] == 0:
                visited[x][y] = cost + 1
                _queue.append([x, y, cost + 1])
_max = -1e9
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            print(-1)
            sys.exit()
        _max = max(_max, visited[i][j])

print(_max)



