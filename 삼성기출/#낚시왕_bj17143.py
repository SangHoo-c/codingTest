from copy import deepcopy
import sys

R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1] = [s, d, z]  # 속력, 이동방향, 크기

dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
# 낚시왕이 오른쪽으로 한 칸 이동한다.
# 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 상어가 이동한다.
ans = 0


def outrange(i, j, fast, d):
    dx, dy = dir[d - 1]
    if d == 1 or d == 2:
        fast = fast % ((R - 1) * 2)
    elif d == 3 or d == 4:
        fast = fast % ((C - 1) * 2)
    while True:
        if -1 < i + dx * fast < R and -1 < j + dy * fast < C:
            return i + dx * fast, j + dy * fast, d

        if d == 1:
            fast -= i  # 가장 위로 만들어주고
            dx, dy = 1, 0  # 방향 바꿔버리기
            i = 0
            d = 2

        elif d == 2:  # 가장 아래로 만들어주고
            fast -= (R - 1 - i)
            dx, dy = -1, 0
            i = R - 1
            d = 1
        elif d == 3:  # 가장 오른쪽으로 만들고
            fast -= (C - 1 - j)
            dx, dy = 0, -1
            j = C - 1
            d = 4
        elif d == 4:  # 가장 왼쪽
            fast -= j
            dx, dy = 0, 1
            j = 0
            d = 3


# 상어를 잡는 낚시꾼
for j in range(C):
    for i in range(R):
        if board[i][j] != 0:
            ans += board[i][j][2]
            board[i][j] = 0
            break

    # 상어의 이동
    new_board = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:  # 상어가 있다면
                fast = board[i][j][0]
                nx, ny, d = outrange(i, j, fast, board[i][j][1])
                if new_board[nx][ny] == 0:  # 아무도 없을때
                    new_board[nx][ny] = [board[i][j][0], d, board[i][j][2]]

                else:  # 있다면 잡아먹으렴...
                    if new_board[nx][ny][2] < board[i][j][2]:
                        new_board[nx][ny] = [board[i][j][0], d, board[i][j][2]]

    board = deepcopy(new_board)

print(ans)
