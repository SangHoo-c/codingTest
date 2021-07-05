# bfs 진행 
# water 와 두더지의 저장소를 다르게 설정 
# go_visited 에 두더지의 경로를 저장 => water 와 두더지를 하나의 경로 배열에 저장한다면, 체크하지 못하는 경우가 존재 

import sys
from collections import deque

read: () = lambda: sys.stdin.readline().strip()

R, C = map(int, read().split(" "))
input_map = [list(map(str, read())) for _ in range(R)]

go_visited = [[0] * C for _ in range(R)]
water_que = deque()
go_que = deque()
dest = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def show_arr(arr, r, c):
    for i in range(r):
        for j in range(c):
            print(arr[i][j], end=" ")
        print()
    print('----------')


def init():
    global x1, y1
    for i in range(R):
        for j in range(C):
            if input_map[i][j] == 'D':
                dest.append([i, j])
            elif input_map[i][j] == 'S':
                go_que.append([i, j])
                x1, y1 = i, j
            elif input_map[i][j] == '*':
                water_que.append([i, j])


def bfs():
    while water_que or go_que:
        w_len = len(water_que)
        while w_len:
            w_len -= 1
            wr, wc = water_que.popleft()
            for i in range(4):
                wr_m = wr + dx[i]
                wc_m = wc + dy[i]
                if 0 <= wr_m < R and 0 <= wc_m < C:
                    if input_map[wr_m][wc_m] == '.':  # 빈칸 또는 두더지가 갔던 길이라면
                        water_que.append([wr_m, wc_m])
                        input_map[wr_m][wc_m] = '*'  # input_map 에 water 의 점령지를 표시한다.

        go_len = len(go_que)
        while go_len:
            go_len -= 1
            gr, gc = go_que.popleft()
            for i in range(4):
                gr_m = gr + dx[i]
                gc_m = gc + dy[i]
                if 0 <= gr_m < R and 0 <= gc_m < C:
                    if input_map[gr_m][gc_m] == '.' and go_visited[gr_m][gc_m] == 0:  # '.' 이고, 방문한적이 없는 경우
                        go_visited[gr_m][gc_m] = go_visited[gr][gc] + 1     # 최단 경로를 구하기 위한 식
                        go_que.append([gr_m, gc_m])
                    if input_map[gr_m][gc_m] == 'D':
                        go_visited[gr_m][gc_m] = go_visited[gr][gc] + 1
                        print(go_visited[gr_m][gc_m])
                        return


    print('KAKTUS')


init()
bfs()
