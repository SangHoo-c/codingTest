import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)

N = int(input())
graph = {i: deque() for i in range(1, N + 1)}
for _ in range(N - 1):
    s, d = map(int, sys.stdin.readline().split())
    graph[s].append(d)
    graph[d].append(s)

M = int(input())
anw = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

_depth = [0] * (N + 1)
_parent = [0] * (N + 1)
_visited = [0] * (N + 1)


# 루트 노드부터 시작하여 깊이를 구하는 함수
# c = _cur_idx
# n = _next_idx
def dfs(c, depth):
    _visited[c] = True
    _depth[c] = depth
    for n in graph[c]:
        if _visited[n]:
            continue
        _parent[n] = c
        dfs(n, depth + 1)


def lca(a, b):
    # 높이를 맞춘다.
    while _depth[a] != _depth[b]:
        if _depth[a] > _depth[b]:
            a = _parent[a]
        else:
            b = _parent[b]

    # 같은 루트를 찾을 때까지 반복한다. 
    while a != b:
        a = _parent[a]
        b = _parent[b]

    return a


if __name__ == '__main__':
    dfs(1, 0)
    for a, b in anw:
        print(lca(a, b))
