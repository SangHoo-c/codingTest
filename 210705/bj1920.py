# O(1) 인 dic 을 활용한 풀이
# 예외처리를 사용하여 답을 계산했다. 

import sys

N = int(input())
_input = list(map(int, sys.stdin.readline().split()))

M = int(input())
_check = list(map(int, sys.stdin.readline().split()))

# dic = {i: 0 for i in range(1, 100001)}
dic = {}
for i in range(N):
    dic[_input[i]] = 1

for i in range(M):
    try:
        if dic[_check[i]] == 1:
            print(1)
    except KeyError:
        print(0)

