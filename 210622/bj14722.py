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
    start_flag = False
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not start_flag and arr[i][j] == 0:
                start_flag = True
                dp[i][j] += 1
                milk[i][j] = 0
                continue

            if start_flag:
                if enable_check(milk[i - 1][j], arr[i][j]):
                    n_milk = dp[i - 1][j] + 1
                    n_last_drink = arr[i][j]

                else:
                    n_milk = dp[i - 1][j]
                    n_last_drink = milk[i - 1][j]

                if enable_check(milk[i][j - 1], arr[i][j]):
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



# ---------------------------------------------------------------------------
# 실패한 풀이 
# 해당 부분은 재귀로 구현한 dfs 풀이 
def get_dp(m, memory, i, j):
    # current_milk = arr[i][j]
    print(m)
    print(' current milk : {} ,'.format(m), end=' ')
    print(' i : {} ,'.format(i), end=' ')
    print(' j : {} ,'.format(j), end='\n')

    if i == 0 and j == 0:
        dp[i][j] = 1
        m = arr[i][j]
        memory = dp[i][j]

    if i + 1 < N:

        if i == 0 and j == 0:
            dp[i][j] = 1
            m = arr[i][j]
            memory = dp[i][j]

        left_milk = arr[i + 1][j]
        if enable_check(m, left_milk):
            dp[i + 1][j] = max(memory + 1, dp[i + 1][j])
            m = arr[i + 1][j]
            memory = dp[i + 1][j]
            get_dp(m, memory, i + 1, j)
        else:
            get_dp(m, memory, i + 1, j)
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
    print(dp)
    if j + 1 < N:
        if i == 0 and j == 0:
            dp[i][j] = 1
            m = arr[i][j]
            memory = dp[i][j]

        right_milk = arr[i][j + 1]
        print([m, right_milk])
        if enable_check(m, right_milk):
            dp[i][j + 1] = max(memory + 1, dp[i][j + 1])
            m = arr[i][j + 1]
            get_dp(m, memory, i, j + 1)
        else:
            get_dp(m, memory, i, j + 1)
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j])

    if i == N - 1 and j == N - 1:
        print('dp 종료!')
        return 0
