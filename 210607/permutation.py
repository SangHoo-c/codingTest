# permutation 
# 길이가 N, 입력받은 문자로 가능한 모든 순열 출력 

import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split(" ")))
arr = sorted(arr)
used = [0] * N
chosen = []


def promising(x):
    if used[x] == 0:
        return True
    else:
        return False


def generate():
    # 2.
    if len(chosen) == N:
        print(chosen)
        return

    # 3.
    for i in range(len(arr)):
        if promising(i):
            chosen.append(arr[i])
            used[i] = 1
            generate()
            used[i] = 0
            chosen.pop()


generate()
