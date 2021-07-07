# 집배원 한상덕
# 1. 투포인터를 사용하여 가능한 높이 pair 를 찾는다.
# 2. 찾은 높이 pair 를 bfs 에 넣어서 가능한지 체크한다.

import sys
from collections import deque

N = int(input())
loc = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
cost = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(N)]
office = []
home = []
height = []
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]


def get_max_min(arr):
    _max = -1e9
    _min = 1e9
    for i in range(N):
        for j in range(N):
            height.append(arr[i][j])
            if int(arr[i][j]) > _max:
                _max = int(arr[i][j])
            if int(arr[i][j]) < _min:
                _min = int(arr[i][j])

    return _max, _min


def get_loc(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'K':
                home.append([i, j])
            elif arr[i][j] == 'P':
                office.append([i, j])
            else:
                continue


# a, b = get_max_min(cost)

def bfs(_min, _max):
    count = 0
    _queue = deque()
    _visited = [[0] * N for _ in range(N)]
    _home_count = len(home)

    # office 의 초기 위치값을 넣어준다.
    _queue.append([office[0][0], office[0][1]])

    while _queue:
        r, c = _queue.popleft()
        for i in range(8):
            x = r + dx[i]
            y = c + dy[i]
            if 0 <= x < N and 0 <= y < N:
                if _min <= cost[x][y] <= _max:
                    if _visited[x][y]:
                        continue
                    else:
                        _visited[x][y] = 1
                        _queue.append([x, y])
                        if loc[x][y] == 'K':
                            count += 1
        if count == _home_count:
            # print('가능!!!')
            return 1

    # print('불가능...')
    return 0


def main():
    global height

    get_loc(loc)
    _max, _min = get_max_min(cost)
    height = list(set(height))
    height.sort()

    # print(height)

    # height 투포인터로 2개씩 고르기
    # _min, _max 값을 변화시키면서 bfs 가 가능한지 체크
    _start = 0
    _end = 0
    _height_len = len(height)
    end_flag = True
    # start 를 차례로 이동하기
    for s in range(_height_len):
        # end 를 가능한 만큼 이동하기, 해당 end 에서 가능하다면 end는 그곳에서 고정
        while _end < _height_len and bfs(height[s], height[_end]) == 0 and end_flag:
            _end += 1
        end_flag = False

        if bfs(height[s], height[_end]) == 0:
            _start = s - 1
            break

    # print(height[_start], height[_end])
    print(abs(height[_start] - height[_end]))


main()
