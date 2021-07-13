# 0. bfs 로 모든 경우를 다 계산해볼 수 있지만, 너무 많은 경우가 나온다. => 다익스트리 알고리즘, 우선순위큐 사용 
# 1. 시작점 초기세팅 ([초기가중치, 시작점])
# 2. queue 에는 모든 가능한 수를 다 집어넣는다. 
# 3. 뺄때 계산을 해준다. 


import sys, heapq
from collections import deque

V, E = map(int, sys.stdin.readline().split())
st = int(input())
graph = {i: deque() for i in range(1, V + 1)}
weight = ['INF'] * (V + 1)

# graph[1][0] = weight, graph[1][1] = destination
for _ in range(E):
    s, d, w = map(int, sys.stdin.readline().split())
    graph[s].append([w, d])


def djs():
    heap = [[0, st]]

    # 초기값

    while heap:
        _cur_w, _cur_idx = heapq.heappop(heap)
        if weight[_cur_idx] == 'INF':
            weight[_cur_idx] = _cur_w
            for _nxt_w, _nxt_idx in graph[_cur_idx]:
                heapq.heappush(heap, [_cur_w + _nxt_w, _nxt_idx])


djs()
for i in range(1, V + 1):
    print(weight[i])
