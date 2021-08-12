"""
  1. 드레곤 커브 표시하기
  2. 체크하기 
  
  사용할 자료구조 선정 : 3차원 배열
  사용할 알고리즘 선정 : 회전행렬, 벡터개념 사용
"""

import sys

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
d_arr = [[[0 for _ in range(4)] for _ in range(101)] for _ in range(101)]


def dragon(x, y, d, g):
    d_list = [[x, y], [x + dx[d], y + dy[d]]]

    for _ in range(g):
        basis = d_list[-1]
        # print(basis, end='@@@\n')
        for i in range(len(d_list) - 2, -1, -1):
            point = d_list[i]
            # 방향 벡터
            v_x = point[0] - basis[0]
            v_y = point[1] - basis[1]

            # 회전변환
            v_x, v_y = -v_y, v_x
            nx = basis[0] + v_x
            ny = basis[1] + v_y
            if not (0 <= nx <= 100 and 0 <= ny <= 100):
                continue
            # 배열 갱신
            d_list.append([nx, ny])

    for idx in range(len(d_list) - 1):
        prv_x, prv_y = d_list[idx]
        nxt_x, nxt_y = d_list[idx + 1]
        dragon_trace(prv_x, prv_y, nxt_x, nxt_y)


def dragon_trace(x, y, nx, ny):
    d_arr[x - 1][y - 1][3] = 1
    d_arr[x - 1][y][1] = 1
    d_arr[x][y][0] = 1
    d_arr[x][y - 1][2] = 1

    d_arr[nx - 1][ny - 1][3] = 1
    d_arr[nx - 1][ny][1] = 1
    d_arr[nx][ny][0] = 1
    d_arr[nx][ny - 1][2] = 1


N = int(input())
for _ in range(N):
    X, Y, D, G = map(int, sys.stdin.readline().split())
    dragon(X, Y, D, G)

result = 0
for i in range(101):
    for j in range(101):
        flag = 0

        for k in range(len(d_arr[i][j])):
            if d_arr[i][j][k]:
                flag += 1
        if flag == 4:
            result += 1
print(result)
