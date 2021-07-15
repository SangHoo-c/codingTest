# 직접 손으로 써보기 
# 그려보기 
# 이해하기 
# 구현하기 

import sys

N = int(input())
num = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]

dp[0][0] = num[0][0]
dp[1][0] = num[1][0] + dp[0][0]
dp[1][1] = num[1][1] + dp[0][0]

for i in range(2, N):
    for j in range(len(num[i])):
        if j == 0:
            dp[i][0] = dp[i-1][0] + num[i][0]
        elif j == i:
            dp[i][i] = dp[i-1][i-1] + num[i][i]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + num[i][j]

print(max(dp[-1]))
