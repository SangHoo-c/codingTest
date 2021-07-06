import sys
from collections import deque
sys.setrecursionlimit(10**6)


def show_arr(ar, I, J):
    for i in range(I):
        for j in range(J):
            print(ar[i][j], end=" ")
        print()
    print('----')


def find_max(ar, I, J):
    _max = -1e9
    for i in range(I):
        for j in range(J):
            _max = max(_max, ar[i][j])
    return _max


N, M = map(int, sys.stdin.readline().split(" "))
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(pos, cnt):
    r = pos[0]
    c = pos[1]

    for i in range(4):
        x = r + dx[i] * int(arr[r][c])
        y = c + dy[i] * int(arr[r][c])

        if 0 <= x < N and 0 <= y < M and arr[x][y] != 'H' and dp[x][y] < cnt + 1:
            if visited[x][y]:
                print(-1)
                exit()
            else:
                dp[x][y] = cnt + 1
                visited[x][y] = 1
                dfs([x, y], cnt + 1)
                visited[x][y] = 0


def main_dfs():
    dfs([0, 0], 0)
    print(find_max(dp, N, M) + 1)

