# bfs 풀이

import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(matrix, cnt, x, y):

    matrix[x][y] = 0

    queue = []
    queue.append((x,y))
    while len(queue) > 0:
        x , y = queue.pop()
        for k in range(0,4):
            nx = x + dx[k]
            ny = y + dy[k]

            if(0 <= nx and nx < n and 0<= ny and ny < n):
                if matrix[nx][ny] == 1:
                    cnt += 1
                    queue.append((nx,ny))
                    matrix[nx][ny] = 0
    return cnt

matrix = [list(map(int, list(read()))) for _ in range(n)]

cnt = 0
ans = []

for i in range(n):
    for j in range(n):

        if(matrix[i][j] == 1):
            ans.append(bfs(matrix, cnt+1, i, j))


print(len(ans))
for x in sorted(ans):
    print(x)
