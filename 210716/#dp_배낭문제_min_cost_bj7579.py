# cost 를 기준으로 배낭 문제 풀기. 
# dp 에 해당 cost 에 가능한 메모리 채워넣기
import sys

N, M = map(int, sys.stdin.readline().split())
mem = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
# cost 의 총합만큼 dp 를 갱신해줘야한다. 
dp = [[0] * (sum(cost)+1) for _ in range(N+1)]
_min = 1e9
for i in range(N):
    for j in range(sum(cost)+1):
        if j >= cost[i]:
            dp[i][j] = max(mem[i] + dp[i-1][j-cost[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

        if dp[i][j] >= M:
            _min = min(_min, j)

print(_min)
