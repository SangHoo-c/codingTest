import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = num[0]
for i in range(1, N):
    dp[i] = dp[i-1] + num[i]    # 해당 부분 O(N) 이기 때문에, 시간안에 들어온다. 

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[b-1] - dp[a-1] + num[a-1])
