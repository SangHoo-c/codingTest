# str1 = ACAYKP
# str2 = CAPCAK 
# 아이디어1. O(n^2) 을 생각했다. str1 문자하나를 기준으로 str2 를 조회해야 하기 때문이다. 
# 아이디어2. 2차원 dp 를 사용해야한다. str2 의 A 를 넣을때 str1[0] , str1[2] 두개의 A 가 있고, 
# 각 케이스를 모두 저장해야하기 떄문에, 1차원 dp 에 담는것은 불가능하다. 

# python 에서 문자열을 다룰경우, 항상 끝에 개행문자가 붙기 떄문에 strip 을 계산해줘야한다. 
# 

import sys

sys.setrecursionlimit(1001)
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

len_A = len(A)
len_B = len(B)

dp = list([0] * (len_B + 1) for _ in range(len_A + 1))

for i in range(0, len_A):
    for j in range(0, len_B):
        if A[i] == B[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1     # dp[i + 1][j + 1] = dp[i+1][j] + 1 여기서 오래 걸렸다. 초기에 설계를 제대로 하자. 
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[-1][-1])
