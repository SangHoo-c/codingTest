# 1. 브루스 포스 
# 2. 서칭 
# DFS -> 재귀형태 한계점, 한쪽 deep 하게 들어갔을때 처리 방법의 애매모호함 
# BFS -> 큐를 사용해 단계별로 깊이를 계산하는 방법
# 가장 오래걸렸던 점, 깊이를 어떻게 설정해주느냐, => queue 에 list 형태로 list[0] : 숫자값, list[1] : 깊이값 을 넣어서 계산. 

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split(" "))


def bfs():
    _queue = deque()
    _queue.append([N, 0])
    _layer = deque()
    visited = set()

    while _queue:
        a = _queue.popleft()
        visited.add(a[0])
        if a[0] == K:
            print(a[1])
            break

        # left = a - 1
        # right = a + 1
        # mul = a * 2
        index = [a[0] - 1, a[0] + 1, a[0] * 2]
        while index:
            tmp = index.pop()
            if tmp not in visited and 0 <= tmp <= 100000:
                _queue.append([tmp, a[1] + 1])

        print(_queue)


bfs()
