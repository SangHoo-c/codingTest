import sys
from collections import deque


# 1.
def move(ar, rob):
    _ar = [0] * 2 * N
    for i in range(-1, 2 * N - 1):
        _ar[i + 1] = ar[i]

    for _ in range(len(rob)):
        r = rob.popleft()
        if r + 1 == N - 1:
            continue
        rob.append(r + 1)

    return _ar


# 2.
def move_robot(ar, rob):
    r_len = len(rob)
    for i in range(r_len):
        r = rob.popleft()
        if (r + 1) in rob:  # robot 이 겹치는 경우
            rob.append(r)
        elif ar[r + 1] == 0:  # 내구도가 없는 경우
            rob.append(r)
        elif ar[r + 1] > 0:  # 겹치지도 않고, 내구도도 있는 경우
            ar[r + 1] -= 1
            if r + 1 == N - 1:
                continue
            rob.append(r + 1)


# 3. 최소한 0 에서 겹치진 않는다.
def upload_robot(ar, rob):
    if ar[0] > 0:
        ar[0] -= 1
        rob.append(0)


# 4.
def check_count(ar):
    cnt = 0
    for a in ar:
        if a == 0:
            cnt += 1

    if cnt == K:
        return 1


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    robot = deque()
    result = 0

    while True:
        result += 1
        arr = move(arr, robot)
        move_robot(arr, robot)
        upload_robot(arr, robot)

        if check_count(arr) == 1:
            print(result)
            break
