# arr[A][B] = arr[A][via] + arr[via][B] 일 수 있다. 

import sys

INF = 1e8 + 1

N = int(input())
M = int(input())

arr = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    i, j, w = map(int, sys.stdin.readline().split())
    if arr[i][j]:
        if arr[i][j] > w:
            arr[i][j] = w

for via in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                arr[i][j] = 0
            # 중간 경로 중에 무한인 값이 없고, 해당 경로를 거쳤을때 값이 작아진다면, 
            if arr[i][via] != INF and arr[via][j] != INF and arr[i][j] > arr[i][via] + arr[via][j]:
                arr[i][j] = arr[i][via] + arr[via][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i][j] == INF:  # 아직 값이 무한이라면, 
            print(0, end=" ")
            continue
        print(arr[i][j], end=" ")
    print()
