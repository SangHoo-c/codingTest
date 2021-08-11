"""
  나무를 하나의 배열에 저장하는 방법 => TLE 
"""

import copy
import sys

N, M, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
for i in range(len(tree)):
    tree[i][0] -= 1
    tree[i][1] -= 1

water = [[5 for _ in range(N)] for _ in range(N)]
dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def show_ar(ar):
    for i in range(N):
        for j in range(N):
            print(ar[i][j], end=" ")
        print()
    print('----')


def spring_summer(t_ar, w_ar):
    for _tree in t_ar:  # 나무들 나이증가
        _x, _y, _age = _tree
        if _age == 0:
            continue
        if _age > w_ar[_x][_y]:  # 죽은 나무 처리
            w_ar[_x][_y] += _age // 2
            _tree[2] = 0
        else:
            w_ar[_x][_y] -= _age
            _tree[2] = _age + 1


def fall(t_ar):
    for _tree in t_ar:
        _x, _y, _age = _tree
        if _age == 0:
            continue
        if _age % 5 == 0:
            for i in range(8):
                r = _x + dx[i]
                c = _y + dy[i]
                if 0 <= r < N and 0 <= c < N:
                    t_ar.append([r, c, 1])


def winter(w_ar):
    for i in range(N):
        for j in range(N):
            w_ar[i][j] += arr[i][j]


for _ in range(K):
    spring_summer(tree, water)
    fall(tree)
    winter(water)
    tree.sort(key=lambda x: ([x[0], x[1], x[2]]))

print(tree)
show_ar(water)
result = 0
for t in tree:
    if t[2] != 0:
        result += 1
print(result)

