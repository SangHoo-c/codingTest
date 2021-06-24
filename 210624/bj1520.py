# O( n ^ 3 ) 시간초과 풀이법 

import sys

N, M = map(int, sys.stdin.readline().split(" "))
ar = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
arr = [[0] * (M + 2) for _ in range(N + 2)]
dp = [[0] * (M + 2) for _ in range(N + 2)]


def init():
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            arr[i][j] = int(ar[i - 1][j - 1])


def dp_init():
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1

            else:
                dp[i][j] = 0

            # west
            if arr[i][j] < arr[i][j - 1]:
                dp[i][j] += dp[i][j - 1]

            # north
            if arr[i][j] < arr[i - 1][j]:
                dp[i][j] += dp[i - 1][j]

            # south
            if arr[i][j] < arr[i + 1][j]:
                dp[i][j] += dp[i + 1][j]

            # east
            if arr[i][j] < arr[i][j + 1]:
                dp[i][j] += dp[i][j + 1]


def show_array(_arr, N, M):
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            print(_arr[i][j], end=" ")
        print()
    print('----')


def main():
    init()
    _iter = N if N > M else M
    # _iter = 4
    for _ in range(_iter):
        dp_init()
    show_array(dp, N, M)
    print(dp[-2][-2])


main()
