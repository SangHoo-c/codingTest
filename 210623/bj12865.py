# knapsack problem. 
# index 처리가 너무 까다로워서 시간이 오래걸렸다. 
# 고정적인 idea 이니, 알아놓을것. 

import sys


def show_dp(ar, N, K):
    for i in range(0, N):
        for j in range(0, K + 1):
            print(ar[i][j], end=' ')
        print()
    print('-----')


N, K = map(int, sys.stdin.readline().split(" "))
weight = [0] * N
value = [0] * N
dp = [[0] * (K + 1) for _ in range(N)]

for i in range(N):
    weight[i], value[i] = map(int, sys.stdin.readline().split(" "))


def main():
    for i in range(N):
        for j in range(K + 1):
            if i == 0:
                if j - weight[i] >= 0:
                    dp[i][j] = value[i]
                continue

            if weight[i] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                if j - weight[i] >= 0:
                    dp[i][j] = max(dp[i - 1][j], value[i] + dp[i - 1][j - weight[i]])
                else:
                    dp[i][j] = max(dp[i - 1][j], value[i] + dp[i - 1][0])

        # show_dp(dp, N, K)
    print(dp[-1][-1])


main()




# --------------------------------
# 효율적인 풀이 

import sys
input = sys.stdin.readline

def knap_sack(N, K):
    dp = {0: 0}
    for _ in range(N):
        W, V = map(int, input().split())
        temp = {}
        for k,v in dp.items():
            # 기존 item의 무게 (k) 와 새로운 item의 무게(W)의 합이 전체 무게(K)보다 작거나 같은 경우
            # 그리고, ? 
            if k + W <= K and v + V > dp.get(k+W,0): # get(key가 없는경우, 'default'값 반환)
                temp[k + W] = v + V

        dp.update(temp)
        
    return max(dp.values())


N, K = map(int, input().split())
print(knap_sack(N, K))
