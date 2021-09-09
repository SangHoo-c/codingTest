"""
  포인트 1. 불필요한 데이터는 저장할 필요가 없다. 
   - 전체 배열 사용 x, 데이터 저장에 queue 사용 
   - 질량이 0 보다 작은경우 저장 x 
   - copy 를 쓰기보다, temp = [] 를 사용하여 데이터를 받는 방법. 
"""

import copy
import sys
from collections import deque


def show_ar(ar):
    print('---')
    for i in range(N):
        for j in range(N):
            print(ar[i][j], end=" ")
        print()
    print('---')


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, sys.stdin.readline().split())
# arr = [[[] for _ in range(N)] for _ in range(N)]
fb = deque()


for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fb.append([r-1, c-1, m, s, d])


for _ in range(K):
    arr = [[[] for _ in range(N)] for _ in range(N)]

    while fb:
        i, j, m, s, d = fb.popleft()
        nx = (i + dx[d] * s) % N
        ny = (j + dy[d] * s) % N
        arr[nx][ny].append([m, s, d])

    # 2. check
    tmp_arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                continue
            m_sum = 0
            s_sum = 0
            flag = set()
            cnt = 0
            for ele in arr[i][j]:
                cnt += 1
                m, s, d = ele
                m_sum += m
                s_sum += s
                if d % 2 == 1:
                    flag.add(1)
                elif d % 2 == 0:
                    flag.add(0)
            if cnt == 1:
                tmp_arr[i][j] = arr[i][j]
                fb.append([i, j, m, s, d])
                continue
            arr[i][j] = []
            nm = m_sum // 5
            ns = s_sum // cnt
            if nm == 0:     # 해당 부분을 넣어서 시간초과를 막았다. 
                continue
            if len(flag) == 1:  # 0, 2, 4, 6
                for k in range(4):
                    tmp_arr[i][j].append([nm, ns, k * 2])
                    fb.append([i, j, nm, ns, k * 2])
            else:  # 1, 3 ,5, 7
                for k in range(4):
                    tmp_arr[i][j].append([nm, ns, k * 2 + 1])
                    fb.append([i, j, nm, ns, k * 2 + 1])
    arr = copy.deepcopy(tmp_arr)
    # show_ar(arr)

# 3. sum
answer = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            for ele in arr[i][j]:
                m, s, d = ele
                answer += m

print(answer)

