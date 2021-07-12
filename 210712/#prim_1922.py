# 1. cur_idx 에서 연결된 모든 노드들을 우선순위 큐에 넣는다. (bfs)
# 2. 우선순위 큐에서 뽑은 값을 확인해서 방문한적이 없는 노드라면, 값을 더한다. 
# 3. 전체 노드 갯수와 방문한 노드 갯수가 같다면 종료한다.


import heapq
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 8)

N = int(input())
M = int(input())
info = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]


graph = defaultdict(int, {i: deque() for i in range(1, N + 1)})

# graph[s][0] => v
# graph[s][1] => d
for s, d, v in info:
    graph[s].append([v, d])
    graph[d].append([v, s])

result = 0
checked = set()
# prim 시도중
heap = []
_cur_idx = 1
checked.add(_cur_idx)

for i in graph[1]:
    heapq.heappush(heap, i)

while True:
    if len(checked) == N:
        break

    while True:
        _next_node = heapq.heappop(heap)
        _next_idx = _next_node[1]
        if _next_idx not in checked:
            checked.add(_next_idx)
            for i in graph[_next_idx]:
                heapq.heappush(heap, i)
            result += _next_node[0]     # 결과 합치기
            break

print(result)
