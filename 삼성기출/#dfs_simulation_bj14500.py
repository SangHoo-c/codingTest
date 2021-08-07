"""
dfs + 특수 케이스 처리하는 방법 

"""

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
mfinger = [[[0, 1], [0, 2], [-1, 1]], [[0, 1], [0, 2], [1, 1]],
           [[1, 0], [2, 0], [1, 1]], [[1, 0], [1, -1], [2, 0]]]
visited = [[0 for _ in range(M)] for _ in range(N)]


def rec(idx, x, y, res, num):
    if idx == 4:
        res.append(num)
        return
    for k in range(4):
        r = x + dx[k]
        c = y + dy[k]
        if 0 <= r < N and 0 <= c < M:
            if not visited[r][c]:
                visited[r][c] = 1
                rec(idx + 1, r, c, res, num + arr[r][c])
                visited[r][c] = 0


def middlefinger(x, y, res):
    for i in mfinger:
        try:
            num = arr[x + i[0][0]][y + i[0][1]] + arr[x + i[1][0]][y + i[1][1]] + arr[x + i[2][0]][
                y + i[2][1]]
        except:
            num = 0
        res.append(num)


def main():
    _max = -1
    for i in range(N):
        for j in range(M):
            result = []
            visited[i][j] = 1
            rec(1, i, j, result, 0)
            visited[i][j] = 0
            middlefinger(i, j, result)

            ij_max = max(result) if result else 0
            _max = max(_max, ij_max + arr[i][j])    #   본인은 가장 나중에 더해주는 방식 

    return _max


print(main())
