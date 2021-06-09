import sys

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split(" ")))
dp = [[] for _ in range(N)]

for i in range(N):
    num_list = [num[i], 1]    # dp 초기화 
    dp[i] = num_list

for i in range(N):
    max_value = -1e9
    for j in range(i):
        if dp[j][0] < dp[i][0]:
            tmp = dp[j][1] + 1
            max_value = max(tmp, max_value)
            dp[i][1] = max_value
        elif dp[j][0] == dp[i][0]:
            dp[i][1] = dp[j][1]
        else:
            continue

dp.sort(key=lambda x: x[1])   # list 안의 원소를 기준으로 정렬 
print(dp[-1][1])
