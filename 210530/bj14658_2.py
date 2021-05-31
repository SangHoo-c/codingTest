# 문제 접근 방법 a. 
# window 를 만들어 차례로 모든 경우를 순회하며 가능한 케이스를 계산한다. 
# N, M <= 500,000 이므로 시간초과. 

# 문제 접근 방법 b. 
# 특이한 꼭짓점에서 시작하는 트램벌린 이외의 예외 케이스를 커버할 알고리즘 필요 
# 트램벌린의 왼쪽 아래 꼭짓점을 별똥별 두개를 O(n^2) 으로 선택하여 정한다. 
# O(k^3) 
# K <= 100 이므로 가능한 알고리즘 

import sys

N, M, L, K = map(int, input().split())
star = []
max_value = -1e9
for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    star.append([x, y])

for i in range(K):
    for j in range(K):
        cnt = 0
        for k in range(K):
            if star[i][0] <= star[k][0] <= star[i][0] + L and star[j][0] <= star[k][1] <= star[j][1] + L:
                cnt += 1
        max_value = max(max_value, cnt)

print(K - max_value)
