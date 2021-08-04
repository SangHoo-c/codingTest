import sys
from collections import deque


def print_ar(ar):
    for i in range(N):
        for j in range(M):
            print(ar[i][j], end=" ")
        print()
    print('-----')


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
wall_cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            wall_cnt += 1


def bfs(ar):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    _queue = deque()
    _safe_cnt = 0
    for i in range(N):
        for j in range(M):
            if ar[i][j] == 2:
                _queue.append([i, j])
                visited[i][j] = 2
            elif ar[i][j] == 1:
                visited[i][j] = 1

    while _queue:
        r, c = _queue.popleft()
        for k in range(4):
            x = r + dx[k]
            y = c + dy[k]

            if 0 <= x < N and 0 <= y < M:
                if ar[x][y] == 0 and not visited[x][y]:
                    _queue.append([x, y])
                    visited[x][y] = 2

    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                _safe_cnt += 1
    return _safe_cnt


_max = -1e9
def comb(cnt, x, y):
    global _max
    if cnt == 3:
        _max = max(_max, bfs(arr))
        return

    for i in range(x, N):
        if i == x:
            for j in range(y, M):
                if not arr[i][j]:
                    arr[i][j] = 1
                    cnt += 1
                    comb(cnt, i, j)
                    cnt -= 1
                    arr[i][j] = 0

        else:
            for j in range(M):
                if not arr[i][j]:
                    arr[i][j] = 1
                    cnt += 1
                    comb(cnt, i, j)
                    cnt -= 1
                    arr[i][j] = 0


comb(0, 0, 0)
print(_max)


