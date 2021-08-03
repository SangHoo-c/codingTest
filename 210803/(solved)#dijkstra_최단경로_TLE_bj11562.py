"""
다익스트라 : 한개의 점에서 모든 점으로 최단경로 => O(n^2)
플로이드-와샬 : 모든 점에서 모든 점으로 최단경로 => O(n^3)
"""

import sys

INF = 1e9
N, M = map(int, sys.stdin.readline().split())
adj = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def init():
    for i in range(1, N + 1):
        adj[i][i] = 0

    for _ in range(M):
        u, v, b = map(int, sys.stdin.readline().split())
        if b == 0:
            adj[u][v] = 0
            adj[v][u] = 1  # 연결통로를 새로 만들어야하는 부분
        elif b == 1:
            adj[u][v] = 0
            adj[v][u] = 0


def main():
    init()
    K = int(sys.stdin.readline())

    # 플로이드-와샬 알고리즘
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if adj[i][j] > adj[i][k] + adj[k][j]:
                    adj[i][j] = adj[i][k] + adj[k][j]

    for _ in range(K):
        s, d = map(int, sys.stdin.readline().split())
        print(adj[s][d])


main()
