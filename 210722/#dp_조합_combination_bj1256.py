import sys

"""
아이디어 
dp[i][j] = "a" i 개, "z" j 개 로 만들 수 있는 조합의 갯수. 
[aazz] = a [azz] + z [aaz]
dp[2][2] = dp[1][2] + dp[2][1]
"""


N, M, K = map(int, sys.stdin.readline().split())
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1
for j in range(M + 1):
    dp[0][j] = 1
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


def main():
    if dp[N][M] < K:
        return -1
    a = N
    z = M
    k = K
    result = ""
    while a or z:
        if a == 0:
            result += "z"
            z -= 1
            continue
        elif z == 0:
            result += "a"
            a -= 1
            continue

        if k <= dp[a - 1][z]:
            result += "a"
            a -= 1
        else:
            result += "z"
            k -= dp[a - 1][z]
            z -= 1

    return result


print(main())
