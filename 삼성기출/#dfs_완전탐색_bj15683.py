import copy
import sys

""" 
    프로세스
    1. CCTV 찾기, 저장
    2. CCTV : n 개 => 4 ^ n 개 dfs 방향배열 만들기 
    3. 각 방향 배열에 따라 check (빈칸 찾기) 수행 
"""

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cctv = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 1.
for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctv.append([arr[i][j], i, j])

cctv_len = len(cctv)
_g_min = 1e9


# 2.
def rec(cnt, ar):
    global _g_min
    if cnt == cctv_len:
        # print(ar)
        input_arr = copy.deepcopy(arr)
        fill(ar, input_arr, cctv)
        _g_min = check(input_arr, _g_min)

        return
    for i in range(4):  # 0 ~ 3 까지의 방향을 자유롭게 넣는다.
        ar.append(i)
        rec(cnt + 1, ar)
        ar.pop()


# 3-1.
def go(ar, x, y, _dr):
    if _dr == 0:
        for j in range(y + 1, M):
            if ar[x][j] == 0:
                ar[x][j] = '#'
            elif ar[x][j] == 6:
                break
    elif _dr == 1:
        for j in range(y - 1, -1, -1):
            if ar[x][j] == 0:
                ar[x][j] = '#'
            elif ar[x][j] == 6:
                break

    elif _dr == 2:
        for i in range(x - 1, -1, -1):
            if ar[i][y] == 0:
                ar[i][y] = '#'
            elif ar[i][y] == 6:
                break
    elif _dr == 3:
        for i in range(x + 1, N):
            if ar[i][y] == 0:
                ar[i][y] = '#'
            elif ar[i][y] == 6:
                break


# 3-2.
def fill(dir_ar, ar, c_ar):  # 각 cctv 의 방향성이 담겨있는 배열 / 전체 배열 / cctv 배열 을 인자로 받는다.
    for i in range(len(dir_ar)):
        _cctv = c_ar[i][0]
        _x = c_ar[i][1]
        _y = c_ar[i][2]
        _dir = dir_ar[i]

        if _cctv == 1:
            go(ar, _x, _y, _dir)
        elif _cctv == 2:
            if _dir == 0 or _dir == 1:
                go(ar, _x, _y, 0)
                go(ar, _x, _y, 1)
            else:
                go(ar, _x, _y, 2)
                go(ar, _x, _y, 3)
        elif _cctv == 3:
            if _dir == 0:
                go(ar, _x, _y, 0)
                go(ar, _x, _y, 2)
            elif _dir == 1:
                go(ar, _x, _y, 1)
                go(ar, _x, _y, 3)
            elif _dir == 2:
                go(ar, _x, _y, 2)
                go(ar, _x, _y, 1)
            elif _dir == 3:
                go(ar, _x, _y, 3)
                go(ar, _x, _y, 0)
        elif _cctv == 4:
            if _dir == 0:
                go(ar, _x, _y, 0)
                go(ar, _x, _y, 1)
                go(ar, _x, _y, 2)
            elif _dir == 1:
                go(ar, _x, _y, 1)
                go(ar, _x, _y, 0)
                go(ar, _x, _y, 3)
            elif _dir == 2:
                go(ar, _x, _y, 1)
                go(ar, _x, _y, 2)
                go(ar, _x, _y, 3)
            elif _dir == 3:
                go(ar, _x, _y, 0)
                go(ar, _x, _y, 2)
                go(ar, _x, _y, 3)
        elif _cctv == 5:
            go(ar, _x, _y, 0)
            go(ar, _x, _y, 1)
            go(ar, _x, _y, 2)
            go(ar, _x, _y, 3)


# 3-3.
def check(ar, _min):
    _tmp = 0
    for i in range(N):
        for j in range(M):
            if ar[i][j] == 0:
                _tmp += 1
    return min(_min, _tmp)


# def show_ar(ar):
#     for i in range(N):
#         for j in range(M):
#             print(ar[i][j], end=" ")
#         print()
#     print("----")


if __name__ == '__main__':
    _comb = []
    rec(0, _comb)
    print(_g_min)

