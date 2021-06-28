import copy
import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split(" "))

# graph = {}
# 이 방법이 아니다. 애초에 value 가 들어갈 list 를 선언해야함

# 인접 행렬 구현 (나중에 해보기)
# 인접 리스트 구현
graph_init = {i: deque() for i in range(1, N + 1)}

# 인접 리스트의 경우, 그냥, 하면 된다.
visited = set()
visited_2 = set()

for _ in range(M):
    v, l = map(int, sys.stdin.readline().split(" "))
    graph_init[v].append(l)
    graph_init[l].append(v)
    # graph.update({v:l})
    # 해당 문법은 Key 가 존재하는 경우, value 를 업데이트 하고, key 가 없으면, 새로 추가한다.

# deque 정렬
for key in graph_init:
    graph_init[key] = deque(sorted(list(graph_init[key])))

# graph_copy = graph_init
graph_copy = copy.deepcopy(graph_init)

result1 = []
result2 = []


# 재귀를 통한 깊이우선탐색 
def dfs(idx, graph=graph_init):
    visited.add(idx)
    result1.append(idx)
    for _node in graph[idx]:
        if _node not in visited:
            visited.add(_node)
            dfs(_node)


# bfs queue 를 이용한 넓이우선탐색 
def bfs(idx, graph=graph_copy):
    visited_2.add(idx)
    result2.append(idx)
    _queue = deque()
    _queue.append(idx)
    while _queue:
        parent_node = _queue.popleft()
        for _node in graph[parent_node]:
            if _node not in visited_2:
                visited_2.add(_node)
                result2.append(_node)
                _queue.append(_node)


dfs(V)
bfs(V)
print(*result1)
print(*result2)
