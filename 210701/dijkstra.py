import sys
import heapq

#  It is very useful is implementing priority queues
#  where the queue item with higher weight is given more priority in processing.

read = lambda: sys.stdin.readline().strip()
N = int(read())
graph = {i: {} for i in range(1, N + 1)}  # dic 을 사용해 graph 구현

for i in range(1, N + 1):
    _input = list(map(int, read().split(" ")))
    for j in range(1, len(_input) // 2):
        graph[_input[0]][_input[2 * j - 1]] = _input[2 * j]  # 주어진 input 에 맞게 그래프의 노드 / 간선 정보를 저장


def dijkstra(_graph, start):
    dis = {_node: float('inf') for _node in _graph}
    dis[start] = 0
    _queue = []
    heapq.heappush(_queue, [dis[start], start])  # 거리순으로 정렬하기 위해

    while _queue:
        par_dis, par_node = heapq.heappop(_queue)

        if dis[par_node] < par_dis:  # 기존의 거리보다 길다면 continue
            continue

        for chi_node, chi_dis in graph[par_node].items():
            tmp_dis = par_dis + chi_dis
            if tmp_dis < dis[chi_node]:
                dis[chi_node] = tmp_dis
                chi_dis = tmp_dis
                heapq.heappush(_queue, [chi_dis, chi_node])

    print(dis)
    key_max = max(dis.keys(), key=(lambda x: dis[x]))
    return key_max, dis[key_max]



key, result = dijkstra(graph, 1)



'''
6
1 2 8 3 1 4 2 -1
2 -1
3 2 5 4 2 -1
4 5 3 6 5 -1
5 6 1 -1
6 1 5 -1
'''
