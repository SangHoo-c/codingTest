import sys

A = list(map(str, sys.stdin.readline().strip()))
B = list(map(str, sys.stdin.readline().strip()))
a_len = len(A)
b_len = len(B)
dp = [[[] for _ in range(a_len+1)] for _ in range(b_len+1)]


for i in range(b_len):
    for j in range(a_len):
        if B[i] == A[j]:
            cur_cnt, cur_str = dp[i-1][j-1] if dp[i-1][j-1] else [0, ""]
            dp[i][j] = [cur_cnt + 1, cur_str + A[j]]
        else:
            cur_left_cnt, cur_left_str = dp[i-1][j] if dp[i-1][j] else [0, ""]
            cur_top_cnt, cur_top_str = dp[i][j-1] if dp[i][j-1] else [0, ""]
            if cur_left_cnt > cur_top_cnt:
                dp[i][j] = [cur_left_cnt, cur_left_str]
            else:
                dp[i][j] = [cur_top_cnt, cur_top_str]

print(dp[-2][-2][0])
print(dp[-2][-2][1])

