"""
  
  1. rotation 손으로 그려보기. 
  2. 작은것부터 구현하기 
  
  tmp 배열을 사용한 rotation. 
  - 돌지 않은 배열은 어떻게 될지?
"""

import copy
import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def show_ar(ar):
    print()
    n = len(ar[0])
    for i in range(n):
        for j in range(n):
            print(ar[i][j], end=" ")
        print()
    print('--')


def rotate(ar, _len, start_x, start_y):
    # _len = 2 란 가정하에 작성
    if _len == 3:
        # print(start_x, start_y, _len)
        pass
    tmp_index = []
    for sp in range((2 ** _len) // 2):
        # starting point = sp
        n = 2 ** _len - sp * 2
        tmp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1):
            tmp[i][n - 1] = ar[sp + start_x][i + sp + start_y]
            tmp[n - 1][n - 1 - i] = ar[i + sp + start_x][n - 1 + sp + start_y]
            tmp[n - 1 - i][0] = ar[n - 1 + sp + start_x][n - 1 - i + sp + start_y]
            tmp[0][i] = ar[n - 1 - i + sp + start_x][sp + start_y]
        # show_ar(tmp)

        for i in range(n - 1):
            ar[i + start_x + sp][n - 1 + start_y + sp] = tmp[i][n - 1]
            ar[n - 1 + start_x + sp][n - 1 - i + start_y + sp] = tmp[n - 1][n - 1 - i]
            ar[n - 1 - i + start_x + sp][0 + start_y + sp] = tmp[n - 1 - i][0]
            ar[0 + start_x + sp][i + start_y + sp] = tmp[0][i]

        # tmp 를 모두 옮겨주는 방법 => 실패, 옮기지 않은 값도 복제가 되기 때
        # for i in range(n):
        #     for j in range(n):
        #         if tmp[i][j] > 0:
        #             ar[i + sp + start_x][j + sp + start_y] = tmp[i][j]


def check_ice(ar):
    n = len(ar[0])
    tmp = []

    for i in range(n):
        for j in range(n):
            if ar[i][j] <= 0:
                continue
            cnt = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if not (0 <= ni < n and 0 <= nj < n):
                    continue
                if ar[ni][nj] > 0:
                    cnt += 1
            if cnt < 3:
                tmp.append([i, j])
    for t in tmp:
        ar[t[0]][t[1]] -= 1
    # print('check ice')
    # show_ar(ar)


def bfs(ar):
    n = len(ar[0])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    que = deque()
    _max_ice = -1
    for i in range(n):
        for j in range(n):
            if ar[i][j] <= 0 or visited[i][j]:
                continue
            _tmp_ice = 0
            visited[i][j] = 1
            que.append([i, j])

            while que:
                r, c = que.popleft()
                _tmp_ice += 1
                # _max_ice = max(ice, _max_ice)
                for k in range(4):
                    nr = r + dx[k]
                    nc = c + dy[k]

                    if not (0 <= nr < n and 0 <= nc < n):
                        continue
                    if visited[nr][nc] or ar[nr][nc] <= 0:
                        continue
                    que.append([nr, nc])
                    visited[nr][nc] = 1
            _max_ice = max(_max_ice, _tmp_ice)

    _tot_ice = 0
    for i in range(n):
        for j in range(n):
            if ar[i][j] > 0:
                _tot_ice += ar[i][j]
    if _max_ice > 1:
        print(_tot_ice)
        print(_max_ice)
    else:
        print(_tot_ice)
        print(0)
    return


if __name__ == '__main__':
    N, Q = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(2 ** N)]
    l_arr = list(map(int, sys.stdin.readline().split()))

    L = len(arr[0])
    for la in l_arr:
        for i in range(L // (2 ** la)):
            for j in range(L // (2 ** la)):
                x = i * (2 ** la)
                y = j * (2 ** la)
                rotate(arr, la, x, y)
        # print('rotate')
        # show_ar(arr)
        # print('check ice')
        check_ice(arr)
        # show_ar(arr)
    # show_ar(arr)
    # print('---')
    bfs(arr)
    # print('--done---')
