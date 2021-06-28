# dfs 백트래킹 문제 
# 오름차순을 구현하기 위해 dfs 의 인자로 현재 idx 값을 넘겨주고, 비교하며 계산한다. 

import sys
from collections import deque


# cnt = 0 부터 시작
def dfs(k, arr, idx, visited, result_arr):
    if len(result_arr) == 6:
        print(* list(result_arr))
        return

    for i in range(k):
        if visited[i] == 0 and idx < i:
            visited[i] = arr[i]
            result_arr.append(arr[i])
            dfs(k, arr, i, visited, result_arr)
            result_arr.pop()
            visited[i] = 0


while True:
    _input = list(map(int, sys.stdin.readline().split()))
    if _input[0] == 0:
        break
    k = _input[0]
    arr = _input[1:]
    visited = [0] * k
    result_arr = deque()
    dfs(k, arr, -1, visited, result_arr)
    print()
