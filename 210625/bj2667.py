# 전형적인 dfs 문제

import sys

sys.setrecursionlimit(100000)

N = int(sys.stdin.readline().strip())
arr = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]


def show_arr(arr, N):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()
    print('-----')


def init():
    for i in range(N):
        num_str = str(sys.stdin.readline().strip())
        for j in range(N):
            arr[i][j] = int(num_str[j])


def dfs(i, j):
    if i < 0 or i > N - 1 or j < 0 or j > N - 1:
        return 0
    if visited[i][j] or arr[i][j] == 0:
        return 0
    visited[i][j] = 1
    return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1) + 1

def main():
    _result_list = []
    init()
    for r in range(N):
        for c in range(N):
            _ele = dfs(r, c)
            if _ele:
                _result_list.append(_ele)
    print(len(_result_list))
    for res in sorted(_result_list):
        print(res)


main()
