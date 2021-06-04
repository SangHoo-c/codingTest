# 브루스 포스, 순열, 조합 모두 시간초과가 난다. 
# 점화식을 찾는다. 
# dp (1~n) 까지의 규칙, greedy (n-1 ~ n) 규칙 

import sys

N = int(sys.stdin.readline().strip())
weight = list(map(int, sys.stdin.readline().split(" ")))
max = 1
weight.sort()

for i in range(N):
    if max >= weight[i]:
        max += weight[i]
    else:
        break
print(max)
