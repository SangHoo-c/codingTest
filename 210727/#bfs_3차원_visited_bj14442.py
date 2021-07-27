import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split(" "))
visited = [[[0 for _ in range(K + 1)] for _ in range(M + 1)] for _ in range(N + 1)]     # 3차원 배열 선언
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    _queue = deque()
    _queue.append([0, 0, K, 1])  # r, c, k, cnt
    visited[0][0][K] = 1

    while _queue:
        r, c, k, cnt = _queue.popleft()
        
        # 종료 조건
        if r == N - 1 and c == M - 1:
            # print("find! ")
            return cnt
        
        for l in range(4):
            new_r = r + dx[l]
            new_c = c + dy[l]

            if 0 <= new_r < N and 0 <= new_c < M:

                # 벽 o
                if arr[new_r][new_c] == "1":
                    if k > 0 and not visited[new_r][new_c][k-1]:
                        visited[new_r][new_c][k - 1] = 1
                        _queue.append([new_r, new_c, k - 1, cnt + 1])

                # 벽 x
                else:
                    if not visited[new_r][new_c][k]:
                        visited[new_r][new_c][k] = 1
                        _queue.append([new_r, new_c, k, cnt + 1])

    # 모든 경우를 해보았음에도 답이 없을 경우
    return -1


print(bfs())
