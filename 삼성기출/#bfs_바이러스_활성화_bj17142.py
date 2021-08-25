
"""
    1. 가능한 바이러스 조합 만들기
    2. bfs 수행
    - 비활성화된 바이러스 만나면, 활성화 시키기. but, max 값은 갱신하지 않는다. 
"""

import sys
from itertools import combinations
from collections import deque

INF = 1e9

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
virus = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def show_arr(ar):
    for i in range(N):
        for j in range(N):
            print(ar[i][j], end=" ")
        print()
    print('-------')


# bfs 수행
def bfs(start_point):
    _max = 0
    _queue = deque()
    _visited = [[INF for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                _visited[i][j] = '*'
            elif arr[i][j] == 1:
                _visited[i][j] = '-'
    for st in start_point:
        _queue.append([st[0], st[1], 0])  # x, y, cost
        _visited[st[0]][st[1]] = 0

    while _queue:
        r, c, cost = _queue.popleft()
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]

            if not (0 <= x < N and 0 <= y < N):
                continue

            if arr[x][y] == 0 and _visited[x][y] > cost + 1:
                _queue.append([x, y, cost + 1])
                _visited[x][y] = cost + 1
                _max = max(_max, cost + 1)
            elif _visited[x][y] == '*':         # 비활성 바이러스 활성 바이러스로 변경
                _queue.append([x, y, cost + 1])
                _visited[x][y] = cost + 1       # max 값은 갱신하지 않는다.

    flag = False
    for i in range(N):
        for j in range(N):
            if _visited[i][j] == INF:
                flag = True
    if flag:
        return -1
    return _max


def main():
    # find virus
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                virus.append([i, j])

    virus_cand = list(combinations(virus, M))

    # 각 virus 조합에 대해 bfs 수행
    res = []

    for v in virus_cand:
        res.append(bfs(v))

    res_v = max(res)
    if res_v == -1:
        res_v = -1
    else:
        for r in res:
            if r != -1:
                res_v = min(res_v, r)
    return res_v


print(main())
