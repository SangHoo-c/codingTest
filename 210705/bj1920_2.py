import sys

N = int(input())
_input = sorted(list(map(int, sys.stdin.readline().split())))

M = int(input())
_check = list(map(int, sys.stdin.readline().split()))


# s 시작 인덱스, l 마지막 인덱스, n 은 찾고자 하는 수
def binary(s, l, n):
    if s > l:
        print(0)
        return

    mid = (s + l) // 2
    if _input[mid] == n:
        print(1)
        return
    elif n < _input[mid]:
        l = mid - 1
    elif n > _input[mid]:
        s = mid + 1
    return binary(s, l, n)


for i in range(M):
    binary(0, N - 1, _check[i])
