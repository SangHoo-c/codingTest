"""
  deque 를 사용해서 
  appendleft 로 왼쪽부터 넣고, 
  일정 값 이상이 되면 idx 를 기억한 후, 
  pop()을 통해 모두 뺀다. 
"""

import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
food = [[5 for _ in range(N)] for _ in range(N)]
node = [[deque() for _ in range(N)] for _ in range(N)]
dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
for t in tree:
    node[t[0] - 1][t[1] - 1].appendleft(t[2])


def spring():
    for i in range(N):
        for j in range(N):
            for k in range(len(node[i][j])):
                if node[i][j][k] <= food[i][j]:
                    food[i][j] -= node[i][j][k]
                    node[i][j][k] += 1
                else:
                    for _ in range(k, len(node[i][j])):
                        food[i][j] += node[i][j].pop() // 2  # summer 역할
                    break


def fall():
    for i in range(N):
        for j in range(N):
            for k in range(len(node[i][j])):
                if node[i][j][k] % 5 == 0:
                    for l in range(8):
                        x = i + dx[l]
                        y = j + dy[l]
                        if 0 <= x < N and 0 <= y < N:
                            node[x][y].appendleft(1)


def winter():
    for i in range(N):
        for j in range(N):
            food[i][j] += arr[i][j]


for _ in range(K):
    spring()
    fall()
    winter()

result = 0
for i in range(N):
    for j in range(N):
        result += len(node[i][j])
print(result)
