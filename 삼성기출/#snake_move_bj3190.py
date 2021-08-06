import sys
from collections import deque, defaultdict

N = int(input())
K = int(input())
apples = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
snack_visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
turn = defaultdict(int)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    apples[r][c] = 1
L = int(input())
for _ in range(L):
    a, b = map(str, sys.stdin.readline().split())
    turn[int(a)] = b

x, y, cur_time, _dir = 1, 1, 0, 0
snake = deque()
snake.append([1, 1])
snack_visited[1][1] = 1
while True:
    # 방향을 바꾸는 방식 
    if turn[cur_time]:
        if turn[cur_time] == 'D':
            _dir = (_dir + 1) % 4
        elif turn[cur_time] == 'L':
            _dir -= 1
            if _dir == -1:
                _dir = 3

    nx = x + dx[_dir]
    ny = y + dy[_dir]

    # 종료조건 1 : 범위를 넘어간 경우 
    if nx < 1 or nx > N or ny < 1 or ny > N:
        print(cur_time + 1)
        break
    # 종료조건 2 : 뱀 본인의 몸통에 부딛힌 경우 
    if snack_visited[nx][ny]:
        print(cur_time + 1)
        break

    # 사과처리
    # 1. 각 자리에 사과는 1개 뿐이다. 
    # 2. 사과가 없는 자리는 queue 를 사용해서 뱀의 길이를 조절한다. 
    if apples[nx][ny]:
        apples[nx][ny] = 0
    else:
        r, c = snake.popleft()
        snack_visited[r][c] = 0
    
    # 다음 코스로 이동하는 뱀 
    snake.append([nx, ny])
    snack_visited[nx][ny] = 1
    x = nx
    y = ny
    cur_time += 1
