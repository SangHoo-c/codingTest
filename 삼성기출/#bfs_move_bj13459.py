"""
bfs 

- 기존 bfs 에서 발전된 점
1. 한칸씩 움직이는 것이 아니라, 여러칸을 한번에 움직인다. 
2. B, R 공의 우선순위에 따라 값이 달라진다. 


"""

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    # init
    _queue = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                rx, ry = i, j
            elif arr[i][j] == 'B':
                bx, by = i, j

    _queue.append([bx, by, rx, ry, 0])
    visited[bx][by][rx][ry] = 1

    # bfs
    while _queue:
        bx, by, rx, ry, tot_cnt = _queue.popleft()
        if tot_cnt >= 10:
            break
        for i in range(4):
            nbx, nby, b_cnt = bx, by, 0
            nrx, nry, r_cnt = rx, ry, 0

            # move 구현
            while arr[nbx][nby] != 'O' and arr[nbx + dx[i]][nby + dy[i]] != '#':
                nbx += dx[i]
                nby += dy[i]
                b_cnt += 1

            # move 구현
            while arr[nrx][nry] != 'O' and arr[nrx + dx[i]][nry + dy[i]] != '#':
                nrx += dx[i]
                nry += dy[i]
                r_cnt += 1

            if arr[nbx][nby] == 'O':
                continue

            if arr[nrx][nry] == 'O':
                print(1)
                return

            if nrx == nbx and nry == nby:
                if r_cnt > b_cnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nbx][nby][nrx][nry]:
                _queue.append([nbx, nby, nrx, nry, tot_cnt + 1])
                visited[nbx][nby][nrx][nry] = 1
    print(0)


bfs()
