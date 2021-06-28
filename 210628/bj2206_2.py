# 다익스트라 
# 스타일을 익혀놓기 

# 맵을 3차원으로 만들어서 세번째 차수에 벽을 뚫었는지 체크 
# flag 정보에 따른 visited 배열 
# visited[x][y][0] => 벽을 꺨 수 '있는' 상태에서, (x,y) 까지의 최소 방문값 
# visited[x][y][1] => 벽을 꺨 수 '없는' 상태에서, (x,y) 까지의 최소 방문값 

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# flag = 1 이면, 벽을 뚫을 수 없는 상태
# flag = 0 이면, 벽을 뚫을 수 있는 상태
def bfs():
    _queue = deque()
    _queue.append([0, 0, 0])
    visited[0][0][0] = 1
    while _queue:
        r, c, flag = _queue.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][flag]

        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]
            if 0 <= x < N and 0 <= y < M:
                # 막혔고, 벽을 꺨 수 있는 상태  
                if arr[x][y] == 1 and flag == 0:
                    visited[x][y][1] = visited[r][c][0] + 1
                    _queue.append([x, y, 1])
                
                # 뚫려있어서, 벽을 꺨 수 있는지가 중요하지 않은 상태 
                if arr[x][y] == 0 and visited[x][y][flag] == 0:
                    visited[x][y][flag] = visited[r][c][flag] + 1
                    _queue.append([x, y, flag])
    return -1


print(bfs())



