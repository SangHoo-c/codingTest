# 구간, 경게값 체크 잘하기 

import sys

R, C, T = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def spread(r, c, ar):
    sp = ar[r][c] // 5
    cnt = 0
    for i in range(4):
        x = r + dx[i]
        y = c + dy[i]

        # 칸을 벗어나거나, 공기청정기가 확산 경로에 있는 경우
        if x < 0 or x > R - 1 or y < 0 or y > C - 1 or ar[x][y] == -1:
            continue
        result[x][y] += sp
        cnt += 1
    result[r][c] += ar[r][c] - (sp * cnt)


for _ in range(T):
    result = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                spread(i, j, arr)

    air_m = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 0:
                arr[i][j] = result[i][j]
                continue
            air_m.append([i, j])

    air_t = air_m[0][0]
    air_b = air_m[1][0]

    tmp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 가장 윗줄, 가장 아랫줄
            if (i == 0 or i == R - 1) and j > 0:
                tmp[i][j - 1] = arr[i][j]
            # top 공기충전기, bottom 공기충전기 라인
            elif (i == air_t or i == air_b) and 0 < j < C - 1:
                tmp[i][j + 1] = arr[i][j]

            # 오른쪽 벽, 위쪽방향
            elif j == C - 1 and 0 < i <= air_t:
                tmp[i - 1][j] = arr[i][j]

            # 오른쪽 벽, 아래방향
            elif j == C - 1 and air_b <= i < R - 1:
                tmp[i + 1][j] = arr[i][j]

            # 왼쪽 벽, 아래방향
            elif j == 0 and i < air_t:
                if i == air_t - 1:
                    continue
                tmp[i + 1][j] = arr[i][j]

            # 왼쪽 벽, 위쪽방향
            elif j == 0 and air_b < i:
                if i == air_b + 1:
                    continue
                tmp[i - 1][j] = arr[i][j]
            else:
                tmp[i][j] = arr[i][j]
    arr = tmp

anw = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            anw += arr[i][j]

print(anw)
