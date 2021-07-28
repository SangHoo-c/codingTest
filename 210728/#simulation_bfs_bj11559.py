"""
디버깅 포인트
1. 한턴에 여러번 터져도 1 count
2. 전체가 같은 색이라면 ? = 터진 count 가 4 이상이어야한다. 
3.. 한번 터진후 내리는 방식 = 세로로 늘어선 방식 & 가로로 늘어선 방식 고려 

"""

import sys
from collections import deque

arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(12)]
arr.append(['.'] * 6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
total_cnt = 0
while True:
    puyo_flag = False
    visited = [[0 for _ in range(6)] for _ in range(12)]

    _queue = deque()
    puyo_1_try_visited = []
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and arr[i][j] != ".":
                _queue.append([i, j, arr[i][j]])
                visited[i][j] = 1
                puyo_cnt = 1
                puyo_visited = [[i, j]]

                while _queue:
                    r, c, cur_m = _queue.popleft()
                    for l in range(4):
                        x = r + dx[l]
                        y = c + dy[l]

                        if 0 <= x < 12 and 0 <= y < 6:
                            if not visited[x][y] and arr[x][y] == cur_m:
                                puyo_cnt += 1
                                _queue.append([x, y, cur_m])
                                visited[x][y] = 1
                                puyo_visited.append([x, y])
                # print(puyo_cnt)

                # puyo 터지는 시점, arr 와 visited 갱신하기 위해 2 중 for 문 빠져나간다.
                if puyo_cnt >= 4:
                    puyo_flag = True
                    puyo_1_try_visited.append(puyo_visited)
    if puyo_flag:
        total_cnt += 1
    if not puyo_flag:
        print(total_cnt)
        break
    
    # puyo 터진 이후 전체 arr 변경하기
    for puyo_visited in puyo_1_try_visited:
        puyo_visited.sort()
        for i in range(12):
            for j in range(6):
                if [i, j] in puyo_visited:
                    for x in range(i-1, -2, -1):
                        if x < 11:
                            arr[x + 1][j] = arr[x][j]
                            

