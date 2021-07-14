import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

def rotate(y, x, height, width):
    global arr
    q = deque()

    for i in range(x, x+width):
        q.append(arr[y][i])
    
    for i in range(y+1, y+height):
        q.append(arr[i][x+width-1])
    
    for i in range(x+width-2, x, -1):
        q.append(arr[y+height-1][i])
    
    for i in range(y+height-1, y, -1):
        q.append(arr[i][x])

    q.rotate(-r)

    for i in range(x, x+width):
        arr[y][i] = q.popleft()
    
    for i in range(y+1, y+height):
        arr[i][x+width-1] = q.popleft()
    
    for i in range(x+width-2, x, -1):
        arr[y+height-1][i] = q.popleft()
    
    for i in range(y+height-1, y, -1):
        arr[i][x] = q.popleft()

height = n
width = m
y, x = 0, 0

while True:
    if height == 0 or width == 0: break

    rotate(y, x, height, width)
    y += 1
    x += 1
    height -= 2
    width -= 2

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()
