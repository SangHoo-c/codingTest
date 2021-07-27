"""
  2번이나 틀린문제, 
  양방향 그래프 설정을 "꼭" 해주자. 
"""

import sys
from collections import deque


def bfs():
    _queue = deque()
    _visited = [0] * (N + 1)
    _queue.append(1)
    _visited[1] = 1
    _cnt = 0
    while _queue:
        _st = _queue.popleft()
        for _n in graph[_st]:
            if not _visited[_n]:
                _queue.append(_n)
                _cnt += 1
                _visited[_n] = 1

    return _cnt


N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
graph = {i: deque() for i in range(1, N + 1)}
for _ in range(V):
    a, b = map(int, sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
print(bfs())
