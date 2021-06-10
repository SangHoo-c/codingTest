# dp 를 2차원으로 선언하여, R G B 의 중복처리를 가능하게 한다. 
# issue. 처음에 문제를 접하고 생각할때, A(n) 을 결정함에 있어서 A(n-2) 까지의 값을 생각했었다. 
# 또한 dp 를 1차원으로 생각해서, R G B 를 처리함에 있어, 총 3^3 = 27 가지의 케이스가 나왔고 이를 min 을 구해야 했다. 
# 가장 중요한 dp 의 사상인, 계산한 케이스를 기억하고 있는 메모리제이션(Memorization) 의 방식의 기법이 아닌, 
# 3 단위로 끊어 min 값을 계산하는 방법이었다. 

# 결론. 
# dp 를 2차원으로 선언하여, 각 케이스의 계산정보를 기억할 수 있게 하고, 이를 바탕으로 A(n) 의 값을 구한다. 

import sys

N = int(sys.stdin.readline())
dp = [[0, 0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    row = list(map(int, sys.stdin.readline().strip().split(" ")))
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + row[0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + row[1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + row[2]

print(min(dp[N]))
