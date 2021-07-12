# 설계의 중요성 
# 경계값 처리 => 매우 민첩하게 반응해야한다. 

from collections import deque
import sys

N = int(input())
K = list(map(int, sys.stdin.readline().split(" ")))

dp = [0] * (N + 1)


def factorial(x):
    if x == 0:
        dp[0] = 1
    else:
        dp[x] = x * factorial(x - 1)
    return dp[x]


def func1():
    n = N
    num = K[1]
    arr = deque(i for i in range(1, N + 1))
    for _ in range(N):
        n -= 1
        div = factorial(n)
        if num == 1:
            while arr:
                print(arr.popleft(), end=" ")
            return
        print(arr[(num - 1) // div], end=" ")
        del arr[(num - 1) // div]
        num %= div

    return


def func2():
    n = N
    per = K[1:]
    arr = deque(i for i in range(1, N + 1))
    result = 0
    for i in range(len(per)):
        n -= 1
        if n < 1:
            result += 1
            print(result)
            break

        mul = factorial(n)
        idx = arr.index(per[i])
        result += mul * idx
        del arr[idx]


flag = K[0]

if flag == 1:
    func1()
else:
    func2()
