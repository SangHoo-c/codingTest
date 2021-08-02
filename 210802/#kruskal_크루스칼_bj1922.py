import sys

N = int(input())
M = int(input())
info = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]

info.sort(key=lambda x: x[2])
parent = [i for i in range(0, N + 1)]
tot_cost = 0


def get_parent(idx):
    if parent[idx] == idx:
        return idx
    else:
        return get_parent(parent[idx])


for s, d, cost in info:
    p_s = get_parent(s)
    p_d = get_parent(d)
    if p_s != p_d:
        tot_cost += cost
        if p_s < p_d:
            parent[p_d] = p_s
        else:
            parent[p_s] = p_d

print(tot_cost)
