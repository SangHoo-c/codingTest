# defaultdict 를 사용하는 방법 
# 2 개의 큰 조합을 만들고 
# 2개를 서로 더해가며 값을 구한다. 

import sys
from collections import defaultdict

T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(" ")))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split(" ")))


def make_comb(arr, N):
    _result = defaultdict(int)
    for i in range(N):
        for j in range(i, N):
            _result[sum(arr[i:j + 1])] += 1

    return _result


def main():
    dict_a = make_comb(A, n)
    dict_b = make_comb(B, m)
    answer = 0

    for key in dict_a.keys():
        answer += dict_b[T - key] * dict_a[key]
    print(answer)


main()
