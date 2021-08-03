import sys
import heapq
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = {i: deque() for i in range(1, N + 1)}
r_graph = {i: deque() for i in range(1, N + 1)}
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(M):
    u, v, b = map(int, sys.stdin.readline().split())
    if b == 0:
        graph[u].append(v)
        r_graph[v].append(u)
    elif b == 1:
        graph[u].append(v)
        graph[v].append(u)

K = int(sys.stdin.readline())


def bfs(x, y):  # x : src, y : dst
    heap = [[0, x]]  # cost, src
    cost = [-1] * (N + 1)
    visited = [0] * (N + 1)
    cost[x] = 0
    visited[x] = 1

    while heap:
        cur_cost, cur_idx = heapq.heappop(heap)
        if cost[cur_idx] == -1:
            cost[cur_idx] = cur_cost
        if cur_idx == y:
            break

        for nxt_idx in graph[cur_idx]:
            if cost[nxt_idx] == -1 and not visited[nxt_idx]:
                heapq.heappush(heap, [cur_cost, nxt_idx])
                visited[nxt_idx] = 1

        for nxt_idx in r_graph[cur_idx]:
            if cost[nxt_idx] == -1 and not visited[nxt_idx]:
                heapq.heappush(heap, [cur_cost + 1, nxt_idx])
                visited[nxt_idx] = 1
    # print(cost)
    print(cost[y])


for _ in range(K):
    s, d = map(int, sys.stdin.readline().split())
    bfs(s, d)

