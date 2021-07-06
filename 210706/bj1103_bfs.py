import sys
from collections import deque
sys.setrecursionlimit(10**6)


def show_arr(ar, I, J):
    for i in range(I):
        for j in range(J):
            print(ar[i][j], end=" ")
        print()
    print('----')


def find_max(ar, I, J):
    _max = -1e9
    for i in range(I):
        for j in range(J):
            _max = max(_max, ar[i][j])
    return _max


N, M = map(int, sys.stdin.readline().split(" "))
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def bfs():
    _queue = deque()
    _queue.append([0, 0])
    visited[0][0] = 0
    while _queue:
        r, c = _queue.popleft()
        if visited[r][c] > N * M:  # 무한번 움직이는 경우
            # 강제 종료
            return -1

        for i in range(4):
            x = r + dx[i] * int(arr[r][c])
            y = c + dy[i] * int(arr[r][c])

            if 0 <= x < N and 0 <= y < M and arr[x][y] != 'H':

                visited[x][y] = visited[r][c] + 1
                _queue.append([x, y])
            else:  # 보드 밖으로 나가거나 / H 에 진입하는 경우
                continue
        # show_arr(visited, N, M)

    # 정상 종료
    return 0


def main_bfs():
    if bfs() == 0:
        print(find_max(visited, N, M) + 1)
    else:
        print(-1)
