# pypy 로 통과함.
# dp[i][j] : i ~ j 까지 행렬의 곱을 했을때 최솟값. 


import sys

N = int(input())
dp = [[0] * (N + 1) for _ in range(N + 1)]
num = [[0, 0]]
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    num.append([a, b])


# l : 왼쪽 좌표
# r : 오른쪽 좌표
def rec(l, r):
    if dp[l][r]:
        return dp[l][r]
    if l == r:
        dp[l][r] = 0
        return dp[l][r]
    if r - l == 1:
        dp[l][r] = num[l][0] * num[l][1] * num[r][1]
        return dp[l][r]

    _min = 1e9
    for k in range(l, r):
        _left = rec(l, k)
        _right = rec(1+k, r)
        _min = min(_min, _left + _right + num[l][0] * num[k][1] * num[r][1])
    dp[l][r] = _min
    return dp[l][r]


print(rec(1, N))
