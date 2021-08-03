import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    _queue = deque()
    _queue.append([0, 0])
    dp[0][0] = 0

    while _queue:
        r, c = _queue.popleft()
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]

            if 0 <= x < N and 0 <= y < M:
                if dp[x][y] == -1 or dp[x][y] > dp[r][c] + int(arr[x][y]):
                    dp[x][y] = dp[r][c] + int(arr[x][y])
                    _queue.append([x, y])

    print(dp[-1][-1])


bfs()
