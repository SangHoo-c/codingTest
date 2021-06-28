# dfs 풀이  => 시간초과
# 가능한 모든 케이스를 다 점검하는 경우 이기때문에 
# M = 1000, N = 1000 인 케이스, 굉장히 많은 가짓수가 나올 수 있음. 
# 언제 dfs 를 쓰는가? => 조합, 백트래킹, 


import sys

sys.setrecursionlimit(100000)

N, M = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result_arr = []


def dfs(r, c, cnt, flag):
    if r < 0 and r >= N and c < 0 and c >= M:
        return 0

    if visited[r][c]:
        return 0

    # 이동 할 수 있는 곳
    if arr[r][c] == 0:
        for i in range(4):
            if 0 <= r + dx[i] < N and 0 <= c + dy[i] < M:
                visited[r][c] = 1

                dfs(r + dx[i], c + dy[i], cnt + 1, flag)
                visited[r][c] = 0
    # 이동 할 수 없는 곳
    if arr[r][c] and flag == 0:
        for i in range(4):
            if 0 <= r + dx[i] < N and 0 <= c + dy[i] < M:
                # flag = 1
                visited[r][c] = 1

                dfs(r + dx[i], c + dy[i], cnt + 1, flag + 1)
                visited[r][c] = 0

    if r == N - 1 and c == M - 1:
        result_arr.append(cnt)


dfs(0, 0, 1, 0)
print(visited)
print(result_arr)
if result_arr:
    print(min(result_arr))
else:
    print(-1)
