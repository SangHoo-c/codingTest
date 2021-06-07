# N <= 10000
# nlogn 정렬 + O(N), 브루스-포스 풀이 
# 오름차순, 내림차순 정렬을 나눠서 계산 

# 특이 케이스 1. 음수간의 곱셈 처리 
# 특이 케이스 2. 숫자(1) 의 곱셈 처리,  ex)  1 * 2 < 1 + 2 

import sys
N = int(sys.stdin.readline().strip())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline().strip()))

anw = 0

# 1 오름차순 배열 정렬 
num.sort()
for i in range(N):
    if i % 2 == 1:
        continue
    if num[i] < 0 and i < N - 1:
        if num[i] * num[i+1] >= 0:
            anw += num[i] * num[i+1]
        else:
            anw += num[i]
            break
    if num[i] < 0 and i == N - 1:
        anw += num[i]

# 2 내림차순 배열 정렬 
num.sort(reverse=True)
for i in range(N):
    if i % 2 == 1:
        continue
    if num[i] >= 0 and i < N -1:
        if num[i] * num[i+1] > 0:
            add = num[i] + num[i+1]
            mul = num[i] * num[i+1]
            anw += max(add, mul)

        else:
            anw += num[i]
            break
    if num[i] >= 0 and i == N - 1:
        anw += num[i]


print(anw)
