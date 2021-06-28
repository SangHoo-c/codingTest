# bfs 문제 
# bfs 에서 매 순서마다 겹쳤던 노드들을 어떻게 처리할지 고민. 
# 각 경로당 최소 값을 visited 에 저장 
# ex) visited[i][j] = i,j 까지 경로의 최소 값 
# 돌아서 오는 값들은 visited 에 값이 있으므로 접근할 수가 없다. 

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []


def bfs(r, c):
    _queue = deque()
    _queue.append([r, c])

    while _queue:
        cur = _queue.popleft()
        # visited[cur[0]][cur[1]] = 1
        # result.append([cur[0], cur[1]])

        for i in range(4):
            r_tmp = cur[0] + dx[i]
            c_tmp = cur[1] + dy[i]
            # idea bfs 에서 겹치는 친구들은 어떻게 처리하는가?
            # visited[i][j] 에 i, j 까지의 비용을 저장한다.
            if r_tmp < 0 or r_tmp > N - 1 or c_tmp < 0 or c_tmp > M - 1 or visited[r_tmp][c_tmp] \
                    or arr[r_tmp][c_tmp] == 0:
                continue
            _queue.append([r_tmp, c_tmp])
            visited[r_tmp][c_tmp] = visited[cur[0]][cur[1]] + 1


bfs(0, 0)
print(visited[-1][-1] + 1)
