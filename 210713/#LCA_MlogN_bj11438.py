# LCA 문제

import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)
LOG = 21  # 2 ^ 20 = 1,000,000

N = int(input())


graph = {i: deque() for i in range(1, N + 1)}
for _ in range(N-1):
    s, d = map(int, sys.stdin.readline().split())
    graph[s].append(d)
    graph[d].append(s)

M = int(input())
anw = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

_depth = [0] * (N + 1)  # 각 노드의 깊이 정보
_parent = [[0] * LOG for _ in range(N + 1)]  # 각 노드의 부모 노드 정보
_visited = [0] * (N + 1)  # 각 노드 방문체크


# 루트 노드부터 시작하여 깊이를 구하는 함수
# c = _cur_idx
# n = _next_idx
def dfs(c, depth):
    _visited[c] = True
    _depth[c] = depth
    for n in graph[c]:
        if _visited[n]:
            continue
        _parent[n][0] = c  # 상하 직속 부모자식 관계 저장
        dfs(n, depth + 1)


def set_parent():
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, N + 1):
            _next_idx = _parent[j][i - 1]
            _parent[j][i] = _parent[_next_idx][i - 1]


def lca(a, b):
    # b 가 더 깊도록 설정
    if _depth[b] < _depth[a]:
        a, b = b, a

    # 높이가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if _depth[b] - _depth[a] >= (1 << i):
            b = _parent[b][i]

    # 부모가 같아 지도록
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if _parent[a][i] != _parent[b][i]:
            a = _parent[a][i]
            b = _parent[b][i]

    # 이후에 부모가 찾고자하는 조상
    return _parent[a][0]


if __name__ == '__main__':
    set_parent()
    for a, b in anw:
        print(lca(a, b))
