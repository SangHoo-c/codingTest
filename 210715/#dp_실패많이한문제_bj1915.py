import sys

sys.setrecursionlimit(10 ** 8)
N, M = map(int, sys.stdin.readline().split())

num = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

_max = 0
for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:
            dp[i][j] = num[i][j]
        elif num[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        _max = max(dp[i][j], _max)

print(_max * _max)
