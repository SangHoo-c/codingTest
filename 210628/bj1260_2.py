import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split(" "))

# graph = {}
# 이 방법이 아니다. 애초에 value 가 들어갈 list 를 선언해야함

# 인접 행렬 구현 (나중에 해보기)
# 인접 리스트 구현
graph = {i: deque() for i in range(1, N + 1)}

# 인접 리스트의 경우, 그냥, 하면 된다.
visited = set()
visited_2 = set()

for _ in range(M):
    v, l = map(int, sys.stdin.readline().split(" "))
    graph[v].append(l)
    graph[l].append(v)
    # 문제에서 linked list 는 단방향이 아닌, 양방향으로 주어졌기 때문에 모두 양방향 처리를 해줘야한다. 
    # 이후 이를 해야만 이후 탐색에서 제대로된 탐색이 작동한다. 
    
    # graph.update({v:l})
    # 해당 문법은 Key 가 존재하는 경우, value 를 업데이트 하고, key 가 없으면, 새로 추가한다.

# deque 정렬
for key in graph:
    graph[key] = deque(sorted(list(graph[key])))

result1 = []
result2 = []


def dfs(idx):
    visited.add(idx)
    result1.append(idx)
    for _node in graph[idx]:
        if _node not in visited:
            visited.add(_node)
            dfs(_node)


def bfs(idx):
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

print(graph)
dfs(V)
bfs(V)
print(*result1)
print(*result2)
