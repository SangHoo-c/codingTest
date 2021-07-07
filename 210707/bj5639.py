# 통과하는 코드와 TLE 나온 코드간의 차이를 분석해보자. 
# 이유? list slicing 의 time complexity => O(k) 

import sys

sys.setrecursionlimit(10 ** 9)

pre = []
while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break


def rec(start, end):
    if start > end:
        return
    root = pre[start]
    if start == end:
        print(root)
        return

    _point = start
    for i in range(start + 1, end + 1):
        if pre[i] < root:
            _point += 1

    rec(start + 1, _point)
    rec(_point + 1, end)
    print(root)


rec(0, len(pre) - 1)




##########################3
# TLE 코드 


import sys

sys.setrecursionlimit(10 ** 9)

pre = []
while True:
    try:
        pre.append(int(sys.stdin.readline().strip()))
    except:
        break


def rec(arr):
    if not arr:
        return
    if len(arr) == 1:
        print(arr[0])
        return

    root = arr[0]
    _point = 1
    for i in range(1, len(arr)):
        if root > arr[i]:
            _point += 1
        else:
            break

    rec(arr[1:_point])
    rec(arr[_point:])
    print(root)


rec(pre)
