import sys


def solution():
    num = []
    N = int(input())
    dp = [0] * (N + 1)
    for _ in range(N):
        num.append(int(sys.stdin.readline()))

    dp[0] = num[0]
    if N == 1:
        print(dp[0])
        return

    # dp[i] : i+1 번째 개단을 올랐을때 최댓값.
    # o x o
    # x o o
    # x x o
    dp[1] = num[0] + num[1]
    for i in range(2, N):     # @@@@@@@ index error 가 났던 지점. 잘 체크하자. N == 1 과 같은 초기 & 경계값들 잘 체크 하자
        dp[i] = max(dp[i - 2], dp[i - 3] + num[i - 1], dp[i - 3]) + num[i]

    print(dp[N - 1])
    return


solution()
