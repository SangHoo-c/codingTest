# dp 문제
import math
import sys

dp = {}


def isPrime(n):
    if n == 1:
        dp[n] = 0
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            dp[n] = 0
            return 0
    dp[n] = 1
    return 1


while True:
    a = int(sys.stdin.readline())
    if a == 0:
        break
    res = 0
    for i in range(a + 1, 2 * a + 1):
        try:
            if dp[i] == 1:
                res += 1
        except:
            if isPrime(i):
                res += 1
    print(res)
