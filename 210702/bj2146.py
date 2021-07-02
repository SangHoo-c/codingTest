# bfs 와 dfs 를 혼용하여 사용하는 문제
# 1. 연결되어 있는 섬을 확인해서 구분한다,
# 2. 모든 땅의 좌표를 시작점으로 bfs 를 사용하여 최단거리를 구한다.
# * 시간복잡도가 아슬 아슬 했다. 
# 더 효율적인 방법이 있을 것이다. 

from collections import deque
import sys

sys.setrecursionlimit(100000)

read: () = lambda: sys.stdin.readline().strip()
N = int(read())
init_map = [list(map(int, read().split())) for _ in range(N)]
country_map = [[0] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def main():
    make_country()
    print(cal_len())


def dfs(r, c, flag):
    if r < 0 or r > N - 1 or c < 0 or c > N - 1:
        return 0
    if init_map[r][c] == 0:
        return 0
    if country_map[r][c]:
        return 0
    country_map[r][c] = flag

    for i in range(4):
        dfs(r + dx[i], c + dy[i], flag)

    return 1


def make_country():
    _flag = 1
    for i in range(N):
        for j in range(N):
            if dfs(i, j, _flag):
                _flag += 1


def bfs(r, c):
    if country_map[r][c] == 0:
        return 0
    visited = [[0] * N for _ in range(N)]
    _flag = country_map[r][c]  # 시작점이 정해진 상태, 위치 : [r,c] , 나라 : flag
    _queue = deque()
    _queue.append([r, c])
    visited[r][c] = 1

    break_flag = False
    while _queue:
        _r, _c = _queue.popleft()
        for i in range(4):
            x = dx[i] + _r
            y = dy[i] + _c
            if x < 0 or x > N - 1 or y < 0 or y > N - 1:
                continue
            if visited[x][y]:  # 이미 방문한 공간이라면
                continue
            if country_map[x][y] != _flag and country_map[x][y]:  # 현재 탐색중인 나라와 다를 경우
                break_flag = True
                break
            _queue.append([x, y])
            visited[x][y] = 1

        if break_flag:
            break

    return abs(x - r) + abs(y - c) - 1


def cal_len():
    result_arr = []
    for i in range(N):
        for j in range(N):
            if country_map[i][j]:
                tmp = bfs(i, j)
                if tmp:
                    result_arr.append(tmp)
    return min(result_arr)


main()
