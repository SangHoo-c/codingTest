"""
1. djs 를 통해 최단 경로를 찾는다.
2. reverse 과정을 통해 최단 경로를 돌아간다. 

* 통과하긴 했으나, refactoring 필요한 코드
"""


import sys, heapq
from collections import deque

N = int(input())
M = int(input())

graph = {i: deque() for i in range(1, N + 1)}
r_graph = {i: deque() for i in range(1, N + 1)}
weight = ['INF'] * (N + 1)

for _ in range(M):
    s, d, c = map(int, sys.stdin.readline().split())
    graph[s].append([c, d])
    r_graph[d].append([c, s])

src, dst = map(int, sys.stdin.readline().split())


def djs():
    heap = [[0, src]]

    while heap:
        _cur_w, _cur_idx = heapq.heappop(heap)
        if weight[_cur_idx] == 'INF':
            weight[_cur_idx] = _cur_w
            for _nxt_w, _nxt_idx in graph[_cur_idx]:
                heapq.heappush(heap, [_cur_w + _nxt_w, _nxt_idx])


def r_djs():
    heap = [[0, dst]]
    visited = [0] * (N + 1)
    result = []
    while heap:
        _cur_w, _cur_idx = heap.pop()
        if visited[_cur_idx] == 0:
            for _nxt_w, _nxt_idx in r_graph[_cur_idx]:
                if weight[_nxt_idx] == weight[_cur_idx] - _nxt_w:
                    visited[_cur_idx] = 1
                    result.append(_cur_idx)
                    heap.append([_nxt_w, _nxt_idx])
                    break

    result.append(src)
    result.reverse()
    print(len(result))
    print(*result)


djs()
print(weight[dst])
# print(weight)
# print(r_graph)
r_djs()
