"""
  1. 먹을 수 있는 물고기가 있는지 체크 (가능여부는 체크하지 않음)
  2. 모든 경우를 bfs 로 탐색한다. 
  3. 가장 적합한 케이스를 뽑는다. 
"""

import sys
import heapq
from collections import deque

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shark_size = 2
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check():  # return 먹을 수 있는 물고기, shark x, shark y
    flag = 0
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                x, y = i, j
                continue
            if 0 < arr[i][j] < shark_size:
                flag += 1
    return flag, x, y


def bfs(x, y):  # shark (x, y) 에서 시작
    heap = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    _queue = deque()
    _queue.append([x, y, 0])
    visited[x][y] = 1
    while _queue:
        i, j, dis = _queue.popleft()
        for l in range(4):
            r = i + dx[l]
            c = j + dy[l]
            if 0 <= r < N and 0 <= c < N and arr[r][c] <= shark_size:  # 이동가능
                if not visited[r][c]:
                    _queue.append([r, c, dis + 1])
                    visited[r][c] = 1
                    if 0 < arr[r][c] < shark_size:  # 먹을 수 있는지
                        heapq.heappush(heap, [dis + 1, r, c])
    if not heap:   
        return 0, x, y
    dis, new_x, new_y = heapq.heappop(heap)
    return dis, new_x, new_y


time = 0
eat_cnt = 0
while True:
    if time == 0:
        fish, shark_x, shark_y = check()
    else:
        fish, _, _ = check()
    if fish == 0:
        print(time)
        break
    arr[shark_x][shark_y] = 0  # 상어 위치 변경
    tmp_x, tmp_y = shark_x, shark_y
    c_time, shark_x, shark_y = bfs(shark_x, shark_y)
    if tmp_x == shark_x and tmp_y == shark_y:   # 상어 위치에 변동이 없을 경우 
        print(time)
        break
    arr[shark_x][shark_y] = 9  # 상어 위치 변경
    eat_cnt += 1
    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0
    time += c_time

