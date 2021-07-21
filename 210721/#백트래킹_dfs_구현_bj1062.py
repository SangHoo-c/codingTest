# main -> dfs -> 각 조합마다 check 호출

import sys

N, K = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
candidate = set()

for word in arr:
    for w in word:
        if w not in {'a', 'n', 't', 'i', 'c'}:
            candidate.add(w)

# nCr 을 위한 변수
candidate = list(candidate)
visited = [0] * len(candidate)
c_arr = []
_max = -1e9


def main():
    if K < 5:
        print(0)
        return

    dfs(0)
    print(_max)


def dfs(x):
    global _max
    if x == K - 5:
        # print(c_arr + ['a', 'n', 't', 'i', 'c'])
        _max = max(_max, check(c_arr + ['a', 'n', 't', 'i', 'c']))
        return
    st = candidate.index(c_arr[-1]) if c_arr else 0
    for i in range(st, len(candidate)):
        if visited[i] == 0:
            visited[i] = 1
            c_arr.append(candidate[i])
            dfs(x+1)
            visited[i] = 0
            c_arr.pop()


def check(_c_arr):
    _cnt = 0
    for _word in arr:
        _flag = True
        for _w in _word:
            if _w not in set(_c_arr):
                _flag = False
                break

        if _flag:
            _cnt += 1
    return _cnt


main()
