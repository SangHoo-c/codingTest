"""
  구현 
  필요한 정보를 deque, dict 에 잘 저장하고 꺼내 사용하는 풀이
  bfs
"""

import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
_queue = deque()
_continue_flag = True
_tot_cnt = -1
while _continue_flag:
    _tot_cnt += 1
    flag = 0
    _continue_flag = False
    _dict = {i: deque() for i in range(1, N ** 2 + 1)}
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # bfs
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue

            # bfs
            flag += 1
            _queue.clear()
            _queue.append([i, j])
            visited[i][j] = flag
            _dict[flag].append([i, j])

            while _queue:
                r, c = _queue.popleft()
                for k in range(4):
                    x = r + dx[k]
                    y = c + dy[k]

                    if 0 <= x < N and 0 <= y < N:
                        if visited[x][y]:
                            continue
                        if L <= abs(arr[x][y] - arr[r][c]) <= R:
                            _queue.append([x, y])
                            visited[x][y] = flag
                            _dict[flag].append([x, y])
                            _continue_flag = True

    # 갱신
    for i in range(1, N ** 2 + 1):
        if not _dict[i]:
            continue
        _sum = 0
        for node in _dict[i]:
            x, y = node
            _sum += arr[x][y]

        _tmp = _sum // len(_dict[i])
        for node in _dict[i]:
            x, y = node
            arr[x][y] = _tmp


print(_tot_cnt)
