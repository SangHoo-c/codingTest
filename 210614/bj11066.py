# x[i, j] 를 i ~ j 까지 더한 값이라고 하자.
# cul 리스트에 누적값을 저장 
# ex) dp[2, 4] 는 누적값 + 각 point 별 차이 값

import sys


T = int(sys.stdin.readline())
K = []
file = []
A = []

for i in range(T):
    K.append(int(sys.stdin.readline()))
    file.append(list(map(int, sys.stdin.readline().split())))

for t in range(T):
    anw = 0
    dp_len = len(file[t]) + 1
    dp = [[0] * dp_len for _ in range(dp_len)]
    cul = [0] * dp_len

    for i in range(1, dp_len):
        cul[i] = cul[i - 1] + file[t][i - 1]

    for n in file[t]:  # file 에 담겨있는 리스트 별 조회
        for i in range(1, dp_len):
            for j in range(i, dp_len):
                min_value = 1e9
                if i == j:
                    # 대각선 값을 0 으로 선정해야한다.
                    dp[i][j] = 0
                elif i > j:
                    dp[i][j] = 0
                else:
                    for k in range(i, j):
                        min_value = min(min_value, dp[i][k] + dp[k + 1][j] + cul[j] - cul[i-1])
                    dp[i][j] = min_value

    for i in range(1, dp_len):
        for j in range(1, dp_len):
            print(dp[i][j], end=" ")
        print()

    print(dp[1][dp_len-1])
