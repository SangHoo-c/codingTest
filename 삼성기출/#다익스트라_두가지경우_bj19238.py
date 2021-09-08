"""
  다익스트라 실수하는 점 

  => 정해놓은 우선순위를 지키기위해선, pop 직후에 해당 요소를 검사해야한다. 
"""

import heapq
import sys

N, M, Fuel = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
mem = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
startX, startY = map(int, sys.stdin.readline().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# mark[][][0] : p 위치
# mark[][][1] : f 위치
mark = [[[0 for _ in range(2)] for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        mark[i + 1][j + 1][0] = arr[i][j]
        mark[i + 1][j + 1][1] = arr[i][j]

for _ in range(M):
    p1, p2, f1, f2 = map(int, sys.stdin.readline().split())
    mark[p1][p2][0] = "p"
    mark[f1][f2][1] = "f"
    mem[p1][p2] = [f1, f2]


def find_p(sx, sy):
    heap = []
    heapq.heappush(heap, [0, sx, sy])  # cost, start-x , start-y
    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visited[sx][sy] = 1
    break_flag = False
    tot_cost = 0
    f_r = 0
    f_c = 0
    while heap:
        cost, r, c = heapq.heappop(heap)
        if mark[r][c][0] == "p":  # pop 하자마자 검사해야함. 
            mark[r][c][0] = 0
            tot_cost = cost
            # print(r, c)
            f_r, f_c = r, c
            break

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if not (1 <= nx <= N and 1 <= ny <= N):
                continue

            # heapq 의 우선순위에 맞게 뽑고 싶다면, pop 한 상태에서 체크해야한다.
            # if mark[nx][ny][0] == "p":  # 찾았다!
            #     mark[nx][ny][0] = 0
            #     break_flag = True
            #     tot_cost = cost + 1
            #     print(nx, ny)
            #     break

            if mark[nx][ny][0] == 1:  # 벽이라면
                continue
            if visited[nx][ny]:  # 방문한적이 있다면
                continue

            heapq.heappush(heap, [cost + 1, nx, ny])
            visited[nx][ny] = 1

    return tot_cost, f_r, f_c


def find_f(sx, sy):
    fx, fy = mem[sx][sy]  # p 에 해당되는 f 가 있는 위치
    heap = []
    heapq.heappush(heap, [0, sx, sy])  # cost, start-x , start-y
    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visited[sx][sy] = 1
    tot_cost = 0
    f_r = 0
    f_c = 0
    while heap:
        cost, r, c = heapq.heappop(heap)
        if r == fx and c == fy:  # 찾았다!
            mark[nx][ny][1] = 0
            tot_cost = cost
            # print(r, c)
            f_r, f_c = r, c
            break

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if not (1 <= nx <= N and 1 <= ny <= N):
                continue

            if mark[nx][ny][0] == 1:  # 벽이라면
                continue
            if visited[nx][ny]:  # 방문한적이 있다면
                continue

            heapq.heappush(heap, [cost + 1, nx, ny])
            visited[nx][ny] = 1
    return tot_cost, f_r, f_c


def main(fuel):
    next_x = 0
    next_y = 0
    for i in range(M):
        if i == 0:
            f, next_x, next_y = find_p(startX, startY)
            if fuel - f < 0 or next_x == 0:
                fuel = -1
                break
            fuel -= f
            f, next_x, next_y = find_f(next_x, next_y)
            if fuel - f < 0 or next_x == 0:
                fuel = -1
                break
            fuel += f

        else:
            f, next_x, next_y = find_p(next_x, next_y)
            if fuel - f < 0 or next_x == 0:
                fuel = -1
                break
            fuel -= f
            f, next_x, next_y = find_f(next_x, next_y)
            if fuel - f < 0 or next_x == 0:
                fuel = -1
                break
            fuel += f
    return fuel


print(main(Fuel))
