# 다시 풀어보기 
# dp 를 채워가는 순서 고려하기 

import sys

read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    num = list(map(int, read().split()))

    dp = list(list(0 for _ in range(n)) for _ in range(n))
    # if n=5
    for k in range(1, n):  # k=1,2,3,4
        for i in range(n - k):  # i=0,1,2,3,4 when k=1
            X, Y = i, i + k
            dp[X][Y] = 1e9
            for j in range(k):
                tmp = dp[X + 1 + j][Y] + dp[X][Y - k + j]
                dp[X][Y] = min(dp[X][Y], tmp)
            dp[X][Y] += sum(num[X:Y + 1])
    print(dp[0][-1])
