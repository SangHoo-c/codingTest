# 이항계수 문제. 
# nCr = n-1Cr + n-1Cr-1 을 이용한다.
# dp 를 사용하여 사전에 계산했던 내용을 다시 써먹는다. 

import sys

N, K = map(int, sys.stdin.readline().split(" "))


def get_binary(n, r):
    # 1.
    cache = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    # 2.
    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(r + 1):
        cache[i][i] = 1

    # 3.
    for i in range(1, n + 1):
        for j in range(1, r + 1):
            cache[i][j] = (cache[i - 1][j] + cache[i - 1][j - 1]) % 10007

    return cache[n][r]


print(get_binary(N, K))


# ref. https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients
