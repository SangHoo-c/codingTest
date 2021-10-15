from collections import deque

"""
모든 간선을 한번씩 끊어본다. 
끊어진 상태 => s / e 각각 을 기점으로 bfs 를 두번 수행해서 각각의 연결된 갯수를 구한다. 

"""


def solution(n, wires):
    answer = -1
    _min = 1e9
    graph = {i: deque() for i in range(1, n + 1)}
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    for s, e in wires:
        graph[s].remove(e)
        graph[e].remove(s)
        left = bfs(s, graph, n)
        right = bfs(e, graph, n)

        graph[s].append(e)
        graph[e].append(s)

        _min = min(_min, abs(left - right))

    answer = _min
    return answer


def bfs(st, graph, n):
    que = deque()
    visited = [0 for i in range(n + 1)]
    que.append(st)
    tot = 1
    visited[st] = 1

    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                que.append(nxt)
                visited[nxt] = 1
                tot += 1
    return tot


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

solution(n, wires)
