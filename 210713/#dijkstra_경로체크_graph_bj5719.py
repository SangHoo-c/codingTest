# 1. djs - cost 정방향 순회, 최단 경로를 저장한다. 
# 2. djs - r_cost 역방향 순회, 최단 경로를 저장한다. 
# 3. bfs - 역방향 bfs, 최단경로가 가능한 구간을 체크한다. (avail 갱신)
# 4. djs - f_cost 정방향 순회, avail 을 참고하여, 최단 경로를 구한다. 

# main idea - 
# A노드와 B노드를 잇는 간선 (A, B)가 최단 경로에 속하는지 보는 방법은
# distance(start, A) + distance(A, B) + distance(B, end) == 최단경로

# Ref. https://chinpa.tistory.com/63

import sys, heapq
from collections import deque


def djs(_s, _cost, _graph):
    heap = [[0, _s]]
    while heap:
        _cur_w, _cur_idx = heapq.heappop(heap)
        if _cost[_cur_idx] == -1:
            _cost[_cur_idx] = _cur_w
            for _nxt_w, _nxt_idx in _graph[_cur_idx]:
                heapq.heappush(heap, [_cur_w + _nxt_w, _nxt_idx])


def bfs():
    _queue = deque()
    _queue.append(end)
    _visited = [0] * V

    while _queue:
        _cur_idx = _queue.popleft()
        _visited[_cur_idx] = 1
        for _nxt_cost, _nxt_idx in r_graph[_cur_idx]:
            if cost[_nxt_idx] + _nxt_cost + r_cost[_cur_idx] == _min_dist:
                avail[_nxt_idx][_cur_idx] = False
            if not _visited[_nxt_idx]:
                _queue.append(_nxt_idx)
                _visited[_nxt_idx] = True


if __name__ == '__main__':
    while True:
        V, E = map(int, sys.stdin.readline().split())
        if V == 0 and E == 0:
            break
        graph = {i: deque() for i in range(V)}
        r_graph = {i: deque() for i in range(V)}

        cost = [-1] * (V + 1)
        r_cost = [-1] * (V + 1)
        start, end = map(int, sys.stdin.readline().split())
        avail = [[0] * V for _ in range(V)]

        # graph[1][0] = weight, graph[1][1] = destination
        for _ in range(E):
            s, d, w = map(int, sys.stdin.readline().split())
            graph[s].append([w, d])
            r_graph[d].append([w, s])
            avail[s][d] = True  # 정방향,연결된 간선을 체크한다.

        djs(start, cost, graph)
        djs(end, r_cost, r_graph)

        # print(cost)
        # print(r_cost)

        _min_dist = cost[end]

        bfs()

        f_cost = [-1] * (V + 1)
        f_heap = [[0, start]]
        while f_heap:
            _c_w, _c_i = heapq.heappop(f_heap)
            if f_cost[_c_i] == -1:
                f_cost[_c_i] = _c_w
                for _n_w, _n_i in graph[_c_i]:
                    if avail[_c_i][_n_i]:
                        heapq.heappush(f_heap, [_c_w + _n_w, _n_i])

        print(f_cost[end])

