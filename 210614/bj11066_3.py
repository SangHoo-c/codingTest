# dp [i][j] 
# i 부터 채워간다. 

import math

t = int(input())


def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            small = math.inf
            for k in range(j - i):
                small = min(small, dp[i][i + k] + dp[i + k + 1][j])
            dp[i][j] = small + sum(arr[i:j + 1])
    print(dp[0][n - 1])


for i in range(t):
    solve()
