import sys

N, M = map(int, sys.stdin.readline().split())
num = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]


dp = [[0] * (N+1) for _ in range(N+1)]    # dp 를 크기를 하나 늘린다. but, 시작점은 0 이다. 따라서 만약 dp[-1][-1]이 나더라도, 0 을 반환한다. 

for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + num[i][j]

for _ in range(M):
    a, b, x, y = map(int, sys.stdin.readline().split())
    result = dp[x][y] - (dp[a-1][y] + dp[x][b-1] - dp[a-1][b-1])
    print(result)


