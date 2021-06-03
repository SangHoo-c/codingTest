# 한칸씩 처리한다. 
# 한번 체크한 점은 다시 돌아보지 않아도 괜찮다. 

import sys


def change_all(x, y, arr):
    for i in range(3):
        for j in range(3):
            arr[x+i][y+j] = 1 - arr[x+i][y+j]
            # if arr[x + i][y + j] == 1:
            #     arr[x + i][y + j] = 0
            # else:
            #     arr[x + i][y + j] = 1

cnt = 0
N, M = map(int, input().split())

n_mat = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
m_mat = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

for i in range(N - 2):
    for j in range(M - 2):
        if n_mat[i][j] != m_mat[i][j]:
            change_all(i, j, n_mat)
            cnt += 1

if m_mat != n_mat:
    print(-1)
else:
    print(cnt)
