import sys
import heapq
from collections import deque

N, M, X = map(int, sys.stdin.readline().split(" "))
graph = {i: deque() for i in range(1, N + 1)}
for _ in range(M):
    s, d, c = map(int, sys.stdin.readline().split(" "))
    graph[s].append([c, d])


def djs(x, y):
    # 초기값
    heap = [[0, x]]
    weight = ['INF'] * (N + 1)
    if x == y:  # 제자리 이동이면, 
        return 0

    while heap:
        _cur_w, _cur_idx = heapq.heappop(heap)
        if weight[_cur_idx] == 'INF':
            weight[_cur_idx] = _cur_w
            if _cur_idx == y:  # 종점에 도달했으면 미리 break. 
                break
            for _nxt_w, _nxt_idx in graph[_cur_idx]:
                heapq.heappush(heap, [_cur_w + _nxt_w, _nxt_idx])
    return weight[y]


_max = -1e9
for i in range(1, N + 1):
    _max = max(_max, djs(i, X) + djs(X, i))

print(_max)
