"""
  back-tracking 다양한 경우가 나올 수 있다. 
  구현 = 외워서 하지 말것
"""

import sys

N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arr1 = []
arr2 = []
_min = 1e9


def rec(idx, ar1, ar2):
    global _min
    if idx == N:
        left = 0
        right = 0
        for i in range(len(ar1)):
            for j in range(i + 1, len(ar1)):
                x = ar1[i]
                y = ar1[j]
                left += arr[x][y] + arr[y][x]

        for i in range(len(ar2)):
            for j in range(i + 1, len(ar2)):
                x = ar2[i]
                y = ar2[j]
                right += arr[x][y] + arr[y][x]
        _min = min(_min, abs(right - left))
        return

    if len(ar1) < N // 2:
        ar1.append(idx)
        rec(idx + 1, ar1, ar2)
        ar1.pop()

    if len(ar2) < N // 2:
        ar2.append(idx)
        rec(idx + 1, ar1, ar2)
        ar2.pop()


rec(0, arr1, arr2)
print(_min)
