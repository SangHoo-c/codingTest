import sys
from collections import deque

N = int(input())
num = [list(map(int, sys.stdin.readline().split())) for _ in range(N - 1)]

graph = {i: deque() for i in range(1, N + 1)}
for s, d in num:
    graph[s].append(d)
    graph[d].append(s)

_queue = deque()
visited = set()
_depth_check = {}


# node : node[0] 노드의 값, node[1] 깊이
# _depth_check 에 각 노드의 깊이를 저장한다.  
def bfs():
    depth = 0
    _queue.append([1, depth])
    visited.add(1)

    while _queue:
        cur_node = _queue.popleft()
        _depth_check[cur_node[0]] = cur_node[1]
        for nxt_idx in graph[cur_node[0]]:
            if nxt_idx not in visited:
                _queue.append([nxt_idx, cur_node[1] + 1])
                visited.add(nxt_idx)


bfs()
print(_depth_check)
