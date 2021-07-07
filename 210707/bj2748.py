N = int(input())
dp = [0] * 91


def fibo(x):
    if x == 0:
        dp[0] = 0
        return 0
    elif x == 1:
        dp[1] = 1
        return 1
    elif x == 2:
        dp[2] = 1
        return 1
    else:
        a = dp[x - 1] if dp[x - 1] else fibo(x - 1)
        b = dp[x - 2] if dp[x - 2] else fibo(x - 2)

        dp[x] = a + b
        return dp[x]


print(fibo(N))
