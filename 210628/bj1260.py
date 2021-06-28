# 인접 리스트로 구현한 dfs, bfs 
# graph 에 deque 로 넣은 값들이 들어가 있다. 
# 더 간단한 방법이 있을 것이다. 찾아보기 


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
    graph_init[key] =  deque(sorted(list(graph_init[key])))

# graph_copy = graph_init
graph_copy = copy.deepcopy(graph_init)

# 인접리스트의 경우 visited 를 어떻게 체크할 것인가? => set 을 사용!
def dfs(idx, graph = graph_init):
    if idx not in visited:
        print(idx, end=" ")
        visited.add(idx)
    # 시작점
    while graph[idx]:
        _v = graph[idx].popleft()

        if _v in visited:
            continue
        print(_v, end=" ")
        visited.add(_v)
        dfs(_v)
    return 0



def bfs(idx, graph = graph_copy):
    if idx not in visited_2:
        print(idx, end=" ")
        visited_2.add(idx)

    _queue = deque()
    _queue.append(idx)
    while _queue:
        _v = _queue.popleft()
        while graph[_v]:
            _node = graph[_v].popleft()
            if _node in visited_2:
                continue
            _queue.append(_node)
            visited_2.add(_node)
            print(_node, end=" ")

    # while graph[idx]:
    #     _v = graph[idx].popleft()
    #     _queue.append(_v)

# print(graph)
dfs(V)
print()
bfs(V)
