import sys
from collections import deque

N, V = map(int, sys.stdin.readline().split(" "))

_graph = {i: deque() for i in range(1, N + 1)}
_chasoo = [0] * (N + 1)
visited = [0] * (N + 1)


def main():
    for _ in range(V):
        n1, n2 = map(int, sys.stdin.readline().strip().split(" "))
        _graph[n1].append(n2)
        _chasoo[n2] += 1

    _queue = deque()
    # 0 차수인 노드들을 넣은 큐를 한번씩 조회하며 진행한다.
    for i in range(1, N + 1):
        if _chasoo[i] == 0:
            _queue.append(i)

    result = []
    while _queue:
        cur_idx = _queue.popleft()
        result.append(cur_idx)

        # next_idx = _graph[cur_idx].popleft()
        for next_idx in _graph[cur_idx]:
            _chasoo[next_idx] -= 1
            if _chasoo[next_idx] == 0:
                _queue.append(next_idx)
    print(*result)


main()
