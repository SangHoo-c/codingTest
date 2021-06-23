# 1. 부루스 포스  
# 2. 서칭 (bfs, dfs) => 2^63 -1 회 만 큼 나온다. 
# 한마디로, 모든 케이스를 다 돌려볼 수 는 없는 경우! 
# dp 문제 
# 손으로 그려보며 규칙 찾기. 

import sys

N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split(" ")))

def show_dp(arr, N):
    for i in range(21):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()
    print('-----')

# dp[i][j] 는  => j 번째 숫자까지 계산했을 때 i 가 나올 수 있는 경우의  수
# 3 <= j <= 100, 0 <= i <= 20,
dp = [[0] * N for _ in range(21)]

def solve():
    # 초기화
    dp[num_list[0]][0] = 1
    for j in range(1, N-1):
        for i in range(21):
            if dp[i][j-1]:
                if i + num_list[j] <= 20:
                    dp[i + num_list[j]][j] = dp[i][j-1] + dp[i + num_list[j]][j]

                if i - num_list[j] >= 0:
                    dp[i - num_list[j]][j] = dp[i][j-1] + dp[i - num_list[j]][j]
        # show_dp(dp, N)
    print(dp[num_list[N-1]][N-2])

solve()
