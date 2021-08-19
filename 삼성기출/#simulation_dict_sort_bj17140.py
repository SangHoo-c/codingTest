"""
  1. r, c 비교, 값 체크
  2. r, c 에 따른 연산 수행
  3. 새로운 배열 새성
"""

import sys

R, C, K = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]


def check(ar):
    for cnt in range(101):
        r = len(ar)
        c = len(ar[0])

        if r >= R and c >= C:
            if ar[R - 1][C - 1] == K:
                print(cnt)
                return

        if r >= c:
            ar = r_func(ar, r, c)
        else:
            ar = c_func(ar, r, c)
    print(-1)
    return


def r_func(ar, r, c):
    _max_len = 0
    for i in range(r):
        ar[i] = sort_algo(ar[i])
        _len = len(ar[i])
        _max_len = max(_len, _max_len)

    new_ar = [[0 for _ in range(_max_len)] for _ in range(r)]
    for i in range(r):
        for j in range(len(ar[i])):
            new_ar[i][j] = ar[i][j]

    return new_ar


def c_func(ar, r, c):
    _max_len = 0
    tmp2 = []
    for j in range(c):
        tmp = []
        for i in range(r):
            tmp.append(ar[i][j])
        tmp = sort_algo(tmp)
        _max_len = max(_max_len, len(tmp))
        tmp2.append(tmp)

    new_ar = [[0 for _ in range(c)] for _ in range(_max_len)]

    for k in range(c):
        for i in range(len(tmp2[k])):
            new_ar[i][k] = tmp2[k][i]

    return new_ar


def sort_algo(ar):
    _dic = {}
    for a in ar:
        try:
            _dic[a] += 1
        except:
            _dic[a] = 1
      
     # dictionary 정렬방법, list 값을 반환 
    _dic = sorted(_dic.items(), key=lambda x: [x[1], x[0]]) 
    r_ar = []
    for i in range(len(_dic)):
        if _dic[i][0] == 0 or _dic[i][1] == 0:
            continue
        r_ar.append(_dic[i][0])
        r_ar.append(_dic[i][1])
    return r_ar


check(arr)
