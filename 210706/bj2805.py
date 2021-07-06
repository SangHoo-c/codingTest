# binary search 사용 

import sys

N, M = map(int, input().split(" "))
num = list(map(int, sys.stdin.readline().split(" ")))
start, end = 1, max(num)

ans = 0
while start <= end:
    mid = (start + end) // 2
    # print(mid)
    _cut = 0
    for n in num:
        if n - mid > 0:
            _cut += (n - mid)
    # print(_cut)
    # print('-----')
    if _cut < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)



