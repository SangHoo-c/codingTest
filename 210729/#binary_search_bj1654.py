"""
1. cache 는 필요없다. left, right 에 값이 다 있기 떄문이다. 
2. sort 가 필요할까? 
3. while 문은 왜 넣었는가? => 어차피 end 값을 줄이며 확인하면 될것이다. 

"""

"""
my first code 
"""

import sys

K, N = map(int, sys.stdin.readline().split(" "))

num = [int(sys.stdin.readline()) for _ in range(K)]
num.sort()


def binary_search(l, r, cache):
    # print(l, r)
    if l > r:
        print(cache)
        # print('no answer')
        return

    _mid = (l + r) // 2
    _check = 0
    for i in range(K):
        _check += num[i] // _mid

    if _check == N:
        _idx = _mid
        while True:
            _cnt = 0
            for j in range(K):
                _cnt += num[j] // _idx

            if _cnt == N:
                _idx += 1
                continue
            else:
                print(_idx - 1)
                return
    elif _check > N:
        binary_search(_mid + 1, r, _mid)
    elif _check < N:
        binary_search(l, _mid - 1, cache)


binary_search(1, num[-1], 1)






"""
my last code
"""

import sys

K, N = map(int, sys.stdin.readline().split(" "))

num = [int(sys.stdin.readline()) for _ in range(K)]


def binary_search(l, r):
    # print(l, r)
    if l > r:
        print(r)
        return

    _mid = (l + r) // 2
    _check = 0
    for i in range(K):
        _check += num[i] // _mid

    if _check >= N:
        binary_search(_mid + 1, r)
    elif _check < N:
        binary_search(l, _mid - 1)


binary_search(1, max(num))
