# 효율적인 dfs 백트래킹 코드 구현 
# c_arr 와 같은 저장소를 전역변수로 사용하고 계속해서 업데이트를 하는 것이 아닌, 
# idx = 지금까지 수행한 이정표, 해당 IDX 보다 큰 요소들을 선택하기 위함. 
# x = 현재 선택한 갯수 

import sys

N, K = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(N)]

# nCr 을 위한 변수
_max = -1e9
learn = [False] * 26
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = True


def main():
    if K < 5:
        print(0)
        return

    dfs(0, 0)
    print(_max)


def dfs(idx, x):
    global _max
    if x == K - 5:
        read_cnt = 0
        for _word in arr:
            for _w in _word:
                if not learn[ord(_w) - ord('a')]:
                    break
            else:
                read_cnt += 1
        _max = max(_max, read_cnt) if _max else read_cnt
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, x + 1)
            learn[i] = False


main()
