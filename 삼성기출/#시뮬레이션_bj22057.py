"""
  핵심은 문제 잘 읽기.
  
  - 예제 케이스가 없는 경우, 매우 헷갈리게 할 수 있다. 
  
  태풍으로 범위 안에 있는 경우만 체크하는 것이 아니라, 
  범위에 관계없이 태풍의 영향을 받는다. 
  
  => 이러한 조건은 문제를 읽으면서 파악해야한다. 
  => 매번 같은 조건으로 문제를 풀려고 하지 말아라. 

"""

import sys

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dust = 0


def show_ar(ar):
    print('---')
    for i in range(N):
        for j in range(N):
            print(ar[i][j], end=" ")
        print()
    print('---')


def in_scope(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    else:
        return False


def rotate(r, c, d):
    for _ in range(d):
        nr = -c
        nc = r
        r, c = nr, nc
    return r, c


tea_pong = [
    [-1, 0, 1],
    [1, 0, 1],
    [-2, -1, 2],
    [-1, -1, 7],
    [1, -1, 7],
    [2, -1, 2],
    [-1, -2, 10],
    [1, -2, 10],
    [0, -3, 5],
    [0, -2, 100]
]


def spread(ar, r, c, d):
    global dust
    total = 0
    dest_x = r + dx[d]
    dest_y = c + dy[d]
    for i, j, per in tea_pong:
        i, j = rotate(i, j, d)
        nr = r + i
        nc = c + j
        if in_scope(nr, nc, N):
            if per == 100:
                ar[nr][nc] += ar[dest_x][dest_y] - total
                # print('hi', ar[dest_x][dest_y] - total)
                continue
            tmp = ar[dest_x][dest_y] * per // 100
            ar[nr][nc] += tmp
            total += tmp
            # print(nr, nc)
        else:
            tmp = ar[dest_x][dest_y] * per // 100
            total += tmp
    ar[dest_x][dest_y] = 0


def main():
    start_x = N // 2
    start_y = N // 2
    _len = 1
    _dir = 0
    break_flag = False

    prv_sum = 0
    for i in range(N):
        for j in range(N):
            prv_sum += arr[i][j]

    while True:
        for i in range(1, _len + 1):
            spread(arr, start_x, start_y, _dir)
            start_x += dx[_dir]
            start_y += dy[_dir]
            # print(start_x, start_y, _dir)
            # show_ar(arr)

            if _len == N:
                if start_x == 0 and start_y == 0:
                    break_flag = True
                    break
        if break_flag:
            # show_ar(arr)
            break

        _dir = (_dir + 1) % 4

        for i in range(1, _len + 1):
            spread(arr, start_x, start_y, _dir)
            start_x += dx[_dir]
            start_y += dy[_dir]
            # print(start_x, start_y, _dir)
            # show_ar(arr)

        _dir = (_dir + 1) % 4
        _len += 1

    _sum = 0
    for i in range(N):
        for j in range(N):
            _sum += arr[i][j]
    print(prv_sum - _sum)


main()
