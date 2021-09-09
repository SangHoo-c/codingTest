"""
  greedy 문제
  
  - 가장 먼저 끝나는 프로세스 
  - 가장 먼저 시작하는 프로세스 
  
  순으로 할당한다. 
  
  why? 
  1 ~ 4 는 1 ~ 5 보다 자식으로 더 많은 프로세스를 가질 수 있고 
  4 ~ 6 은 5 ~ 6 보다 부모로 더 많은 프로세스를 가질 수 있기 때문 .
  
"""

import sys

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append([a, b])

arr.sort(key=lambda x: [x[1], x[0]])

ans = 0
cur_idx = 0
for i in range(N):
    if i == 0:
        cur_idx = arr[0][1]
        ans += 1
    else:
        if arr[i][0] >= cur_idx:
            cur_idx = arr[i][1]
            ans += 1

print(ans)
