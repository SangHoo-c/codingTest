import sys

"""
    크루스칼 알고리즘
    1. 간선의 비용이 낮은 순으로 정렬
    2. 낮은 순으로 root 를 찾으며 (find)
    3. 합친다. (union) 
"""

V, E = map(int, sys.stdin.readline().split())
parent = [0] * (V + 1)
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

# 간선의 가중치가 작은 순으로 정렬 
arr.sort(key=lambda x: x[2])


def get_parent(idx):    # find 구현 
    if parent[idx] == idx:
        return idx
    parent[idx] = get_parent(parent[idx])
    return parent[idx]


# parent 초기화
for i in range(1, V + 1):
    parent[i] = i

tot_cost = 0
for e in arr:       # e[0] : src, e[1] : dst, e[2] : cost
    p_s = get_parent(e[0])
    p_d = get_parent(e[1])
    if p_s != p_d:   # parent 가 다르다면, union 
        tot_cost += e[2]
        if p_s < p_d:
            parent[p_d] = p_s
        else:
            parent[p_s] = p_d
print(tot_cost)
