import sys, heapq
from collections import deque

N = int(input())
M = int(input())

graph = {i: deque() for i in range(1, N + 1)}
r_graph = {i: deque() for i in range(1, N + 1)}
weight = [1e9] * (N + 1)
path = [[] for _ in range(N + 1)]

for _ in range(M):
    s, d, c = map(int, sys.stdin.readline().split())
    graph[s].append([c, d])
    r_graph[d].append([c, s])

src, dst = map(int, sys.stdin.readline().split())


def djs():
    heap = [[0, src]]
    path[src].append(src)

    while heap:
        _cur_w, _cur_idx = heapq.heappop(heap)
        if _cur_w > weight[_cur_idx]:
            continue
        if _cur_idx == src:
            weight[_cur_idx] = 0
        for _nxt_w, _nxt_idx in graph[_cur_idx]:
            path_cost = _nxt_w + _cur_w
            if weight[_nxt_idx] > path_cost:
                weight[_nxt_idx] = path_cost
                heapq.heappush(heap, [path_cost, _nxt_idx])
                path[_nxt_idx] = []
                for p in path[_cur_idx]:  # path 가 갱신되었을때, 현재까지의 경로를 넣어준다.
                    path[_nxt_idx].append(p)
                path[_nxt_idx].append(_nxt_idx)


djs()
# print(weight)
print(weight[dst])
print(len(path[dst]))
print(*path[dst])
