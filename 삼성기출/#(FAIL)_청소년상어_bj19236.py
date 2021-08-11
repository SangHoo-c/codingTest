import sys, copy

sys.setrecursionlimit(10 ** 8)

# 0 은 상어의 현재 위치, 1 ~ 16 생선의 위치
loc = {i: [] for i in range(17)}
fish = [[0 for _ in range(4)] for _ in range(4)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
for i in range(4):
    for j in range(4):
        fish[i][j] = arr[i][2 * j]
        loc[arr[i][2 * j]] = [arr[i][2 * j + 1] - 1, i, j]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def move():
    # 1 ~ 16 fish 이동.
    for i in range(1, 17):
        if not loc[i]:
            continue
        cur_fn = i
        d, x, y = loc[i]
        for l in range(8):
            nx = x + dx[(d + l) % 8]
            ny = y + dy[(d + l) % 8]
            if 0 <= nx < 4 and 0 <= ny < 4:
                nxt_fn = fish[nx][ny]
                if nxt_fn == 0:  # 상어라면,
                    continue
                elif nxt_fn == -1:  # 빈칸이라면
                    loc[cur_fn][0] = (d + l) % 8
                    fish[nx][ny], fish[x][y] = fish[x][y], fish[nx][ny]
                    break
                else:  # 정상상태
                    loc[cur_fn][0] = (d + l) % 8
                    fish[nx][ny], fish[x][y] = fish[x][y], fish[nx][ny]
                    for k in range(1, 3):
                        loc[cur_fn][k], loc[nxt_fn][k] = loc[nxt_fn][k], loc[cur_fn][k]
                    break


def rec(ar, fish):
    global tot_cost
    prv_fish = copy.deepcopy(fish)
    # 2. 물고기 이동
    move()

    # 2-1. 상어 이동가능 여부 체크
    cur_s_d, cur_s_x, cur_s_y = loc[0]
    p_flag = False
    for i in range(1, 4):
        n_x = cur_s_x + dx[cur_s_d] * i
        n_y = cur_s_y + dy[cur_s_d] * i

        if 0 <= n_x < 4 and 0 <= n_y < 4:
            if fish[n_x][n_y] > 0:
                p_flag = True
                break
    if not p_flag:  # 종료조건
        print(tot_cost)
        tot_cost = 0
        return

    print(ar)

    s_d, s_x, s_y = loc[0]
    for i in range(1, 4):
        nx = s_x + dx[s_d] * i
        ny = s_y + dy[s_d] * i

        if 0 <= nx < 4 and 0 <= ny < 4:
            nxt_fn = fish[nx][ny]
            if nxt_fn == -1:
                continue
            nxt_fish = loc[fish[nx][ny]]
            prv_shark = loc[0]

            ar.append(fish[nx][ny])
            loc[0] = [nxt_fish[0], nxt_fish[1], nxt_fish[2]]
            fish[s_x][s_y] = -1
            fish[nx][ny] = 0
            tot_cost += nxt_fn
            rec(ar, fish)
            tot_cost -= nxt_fn
            fish = copy.deepcopy(prv_fish)
            ar.pop()
            loc[0] = [prv_shark[0], prv_shark[1], prv_shark[2]]
            fish[nx][ny] = nxt_fn
            fish[s_x][s_y] = 0




# 1. 초기값
tot_cost = 0
loc[0] = [arr[0][1] - 1, 0, 0]  # 상어를 (0, 0) 자리에 넣는다.
loc[arr[0][0]] = []
fish[0][0] = 0  # 상어의 현재 위치
tot_cost += arr[0][0]
cost = []
rec(cost, fish)
# while True:
#     # 2. 물고기 이동
#     move()
#
#     # 2-1. 상어 이동가능 여부 체크
#     cur_s_d, cur_s_x, cur_s_y = loc[0]
#     p_flag = False
#     for i in range(1, 4):
#         n_x = cur_s_x + dx[cur_s_d] * i
#         n_y = cur_s_y + dy[cur_s_d] * i
#
#         if 0 <= n_x < 4 and 0 <= n_y < 4:
#             if fish[n_x][n_y] > 0:
#                 p_flag = True
#                 break
#     if not p_flag:  # 종료조건
#         print(tot_cost)
#         break
#
#     cost = []
#     # 3. 상어 이동
#     rec(cost)
#     break
