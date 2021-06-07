# 처음 생각했던 재귀 방식 풀이 => 예외 case 존재
# N <= 10 인 여유로운 조건에선, 브루스-포스 방법 먼저 생각하기 
# 순열 풀이도 가능해보인다. => 모든 케이스 10! 나열후, 조건에 맞게 체크

import sys

N = int(sys.stdin.readline().strip())
height = list(map(int, sys.stdin.readline().split(" ")))

res = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if res[j] == 0 and cnt == height[i]:
            res[j] = i + 1
            break
        elif res[j] == 0:
            cnt += 1
        else:
            continue

for i in res:
    print(i, end=" ")
