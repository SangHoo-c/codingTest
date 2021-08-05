from collections import deque


def solution(m, n, board):
    answer = 0

    arr = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dx = [0, 1, 1, 0]
    dy = [0, 0, 1, 1]
    for i in range(m):
        for j in range(n):
            arr[i][j] = board[i][j]

    _queue = deque()
    while True:
        visited = [[0 for _ in range(n)] for _ in range(m)]
        tmp_flag = True
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0:
                    continue
                _queue.append([i, j, arr[i][j]])
                while _queue:
                    r, c, fri = _queue.popleft()
                    if arr[r + 1][c] == fri and arr[r + 1][c + 1] == fri and arr[r][c + 1] == fri:
                        if r + 1 < m and c + 1 < n:
                            tmp_flag = False
                            for k in range(1, 4):
                                _queue.append([r + dx[k], c + dy[k], fri])
                            for k in range(4):
                                visited[r + dx[k]][c + dy[k]] = 1

        # move down
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    answer += 1
                    for k in range(i, -1, -1):
                        arr[k][j] = arr[k - 1][j]





        # for i in range(m):
        #     for j in range(n):
        #         print(arr[i][j], end=" ")
        #     print()
        # print('-----')

        if tmp_flag:
            break

    return answer
