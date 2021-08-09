import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
like_dict = {}
answer = 0

for _ in range(N ** 2):
    s_list = list(map(int, sys.stdin.readline().split()))
    like_dict[s_list[0]] = s_list[1:]
    s_num = s_list[0]
    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1

    for i in range(N):
        for j in range(N):
            like_cnt = 0
            empty_cnt = 0
            if arr[i][j] == 0:
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < N and 0 <= y < N:
                        if arr[x][y] in like_dict[s_num]:
                            like_cnt += 1
                        if arr[x][y] == 0:
                            empty_cnt += 1

                if max_like < like_cnt or (max_like == like_cnt and max_empty < empty_cnt):
                    max_x = i
                    max_y = j
                    max_like = like_cnt
                    max_empty = empty_cnt
    arr[max_x][max_y] = s_num


for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < N and 0 <= y < N:
                if arr[x][y] in like_dict[arr[i][j]]:
                    cnt += 1
        if cnt != 0:
            answer += 10 ** (cnt - 1)
print(answer)


"""
  ref. https://jungeun960.tistory.com/201
"""
