import sys

MOD = 100000

C, R = map(int, sys.stdin.readline().split())
dp = [[[[0] * 2 for _ in range(2)] for _ in range(C)] for _ in range(R)]
# dp[r][c][dir - 0(위에서 아래로), 1(왼에서 우로)][rotation - 0(불가능) , 1(가능)]
for i in range(R):
    dp[i][0][0][1] = 1
for j in range(C):
    dp[0][j][1][1] = 1

for i in range(1, R):
    for j in range(1, C):
        # 위에서 아래로 dir - 0
        dp[i][j][0][0] = dp[i - 1][j][1][1]
        dp[i][j][0][1] = (dp[i - 1][j][0][1] + dp[i - 1][j][0][0]) % MOD

        # 왼에서 우로 dir - 1
        dp[i][j][1][0] = dp[i][j - 1][0][1]
        dp[i][j][1][1] = (dp[i][j - 1][1][1] + dp[i][j - 1][1][0]) % MOD

print((sum(dp[-1][-1][0]) + sum(dp[-1][-1][1])) % MOD)
