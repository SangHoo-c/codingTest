# 재귀를 활용하여 푼 문제, 

import sys
sys.setrecursionlimit(10**9)
N, R = map(int, input().split(" "))

dp = [[0] * (R + 1) for _ in range(N + 1)]


def binary(n, r):
    if n < 1 or 1000 < n or r < 0 or 1000 < r or n < r:
        return 0
    if r == 1:
        dp[n][r] = n
        return n
    if n == r or r == 0:
        dp[n][r] = 1
        return 1
    if dp[n][r] == 0:
        dp[n][r] = (binary(n - 1, r) + binary(n - 1, r - 1)) % 10007
    return dp[n][r]


print(binary(N, R))
