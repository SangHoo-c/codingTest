"""
  완전탐색 dfs 의 경우, 굉장히 많은 요소를 탐색하기 떄문에 \
  한가지 조건문을 잘못달아줄 경우, 바로 시간초과가 난다. 
  
  ex) 
  dfs 초기 조건문 해당 구문에서 cnt > 3 으로 해뒀기에, 
  깊이를 하나 더 들어가는 방식이었는데 이는 굉장한 소스 낭비를 한다. 
  따라서 깊이 하나를 들어갈때는 신중하게 조건문을 다는것이 좋다. 

"""

import sys

N, M, H = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(N + 1)] for _ in range(H + 2)]  # 사다리 배열
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    arr[x][y] = 1  # 사다리 왼쪽
    arr[x][y + 1] = 2  # 사다리 오른쪽


def check(ar):  # i => i 라면 return 1, else return 0
    for idx in range(1, N + 1):
        st = idx
        for i in range(1, H + 1):
            if ar[i][st] == 1:
                st += 1
            elif ar[i][st] == 2:
                st -= 1
        if st != idx:
            return 0
    return 1


result = []


def rec(cnt, ar, r, c, res):
    # 기존 코드 => TLE 
    # if cnt > 3:
    #     res.add(-1)
    #     return
    # if check(ar):
    #     res.add(cnt)
    #     return cnt
    
    # 개선된 코드 
    if check(ar):
        res.add(cnt)
        return cnt
    if cnt == 3:
        res.add(-1)
        return
    else:
        for i in range(1, H + 1):
            for j in range(1, N):
                if i < r:
                    continue
                if i == r:
                    if j < c:
                        continue
                if ar[i][j - 1] != 1 and ar[i][j] == 0 and ar[i][j + 1] != 1:
                    ar[i][j] = 1
                    ar[i][j + 1] = 2
                    rec(cnt + 1, ar, i, j, res)
                    ar[i][j] = 0
                    ar[i][j + 1] = 0


result = set()
rec(0, arr, 1, 1, result)
_min = 10
for res in result:
    if res >= 0:
        _min = min(_min, res)

if _min == 10:
    print(-1)
else:
    print(_min)
