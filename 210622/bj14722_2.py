import sys

N = int(sys.stdin.readline().strip())
arr_ = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
arr = [[-1] * (N + 1) for _ in range(N + 1)]
for k in range(1, N + 1):
    for z in range(1, N + 1):
        arr[k][z] = arr_[k - 1][z - 1]

dp = [[0] * (N + 1) for _ in range(N + 1)]
milk = [[-1] * (N + 1) for _ in range(N + 1)]


def show_arr(ar, N):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(ar[i][j], end=' ')
        print()


def enable_check(a, b):
    if a == 0 and b == 1:
        return True
    if a == 1 and b == 2:
        return True
    if a == 2 and b == 0:
        return True
    else:
        return False


def main():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            n_milk = milk[i - 1][j]
            l_milk = milk[i][j - 1]
            current_milk = arr[i][j]

            if current_milk == 0 and n_milk == -1 and l_milk == -1:
                dp[i][j] += 1
                milk[i][j] = 0
                continue

            else:
                if enable_check(n_milk, current_milk):
                    n_milk = dp[i - 1][j] + 1
                    n_last_drink = arr[i][j]

                else:
                    n_milk = dp[i - 1][j]
                    n_last_drink = milk[i - 1][j]

                if enable_check(l_milk, current_milk):
                    l_milk = dp[i][j - 1] + 1
                    l_last_drink = arr[i][j]

                else:
                    l_milk = dp[i][j - 1]
                    l_last_drink = milk[i][j - 1]

                if n_milk > l_milk:
                    milk[i][j] = n_last_drink
                    dp[i][j] = n_milk
                else:
                    milk[i][j] = l_last_drink
                    dp[i][j] = l_milk

                # print([i, j], end="번쨰 \n")
                # show_arr(dp, N)
                # print('drink! {}'.format(milk[i][j]))
                # print(' ---- ')

    # show_arr(dp, N)
    print(dp[-1][-1])


main()




# ------------------------------------------------
# 간단한 풀이, 핵심 

n=int(input())
m=[list(map(int,input().split())) for _ in range(n)]
d=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        d[i][j]=max(d[i-1][j],d[i][j-1])
        if d[i][j]%3==m[i-1][j-1]:d[i][j]+=1
print(d[-1][-1])
