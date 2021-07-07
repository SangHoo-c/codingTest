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

    # 1. 불가능 풀이 (본래 풀이)
    # for _arr_l in range(1, N + 1):
    #     for j in range(N):
    #         _key = 0
    #         if j + _arr_l <= N:
    #             for x in range(j, j + _arr_l):
    #                 _key += arr[x]
    #         if not _key:
    #             continue
    #         _result[_key] = _result.get(_key, 0) + 1
    #         # _result[_key] += 1

    # 2. 가능한 풀이 (개선된 풀이)
    for i in range(N):
        for j in range(i, N):
            _result[sum(arr[i:j + 1])] += 1

    return _result


def main():
    dict_a = make_comb(A, n)
    dict_b = make_comb(B, m)

    # 1번도 가능 (본래 풀이)
    # _count = 0
    # for _b in dict_b.items():
    #     t = T - _b[0]
    #     _a_val = dict_a.get(t, 0)
    #     if _a_val:
    #         _count += _a_val * _b[1]
    # print(_count)

    # 2 번도 가능 (개선된 풀이)
    answer = 0

    for key in dict_a.keys():
        answer += dict_b[T - key] * dict_a[key]
    print(answer)


main()
