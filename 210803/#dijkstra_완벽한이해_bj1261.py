"""
기본 bfs : 340 ms
다익스트라 : 140 ms 

**TIP**
1. heap 에 우선 넣어두고 우선순위에 맞게 나중에 꺼낸다. 
2. 대신 heap 에 넣은 순간, visited 를 체크하여서, 중복으로 heap 에 들어가지 않도록 한다. 
"""


import sys
import heapq
from collections import deque

INF = 1e9
M, N = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def djs():
    heap = [[0, [0, 0]]] # [cost, [r, c]]
    dp[0][0] = 0

    while heap:
        prv_cost, [r, c] = heapq.heappop(heap)
        if dp[r][c] == -1:
            dp[r][c] = prv_cost
        if r == N - 1 and c == M - 1:
            break
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]

            if 0 <= x < N and 0 <= y < M:
                if dp[x][y] == - 1 and not visited[x][y]:
                    heapq.heappush(heap, [prv_cost + int(arr[x][y]), [x, y]])
                    visited[x][y] = 1

    print(dp[-1][-1])


djs()
