import sys


def _update(i, dif):
    while i <= N:
        tree[i] += dif
        i += (i & -i)


def _sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))

    leaf = [0] * (N + 1)
    tree = [0] * (N + 1)

    for i in range(1, N + 1):
        leaf[i] = num[i - 1]
        _update(i, num[i - 1])
    # print(tree)
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        print(_sum(b) - _sum(a-1))    # a <= x <= b 구간 
