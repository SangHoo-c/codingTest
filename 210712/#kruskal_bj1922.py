# kruskal 알고리즘, 익숙해지기 
# 1. 모든 간선을 가중치를 기준으로 정렬한다. 
# 2. 가중치가 낮은 값부터 간선을 연결한다.
# 2-1. 간선 연결시에 root 를 확인해서 서로 다른 값이면 연결한다. => root 를 갱신해준다. 
# 2-2. root 가 같은 경우, 연결하지 않는다. 

import sys

sys.setrecursionlimit(10 ** 8)

N = int(input())
M = int(input())
info = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]

# kruskal
root = [i for i in range(N + 1)]

# 낮은 비용 순으로 정렬
info.sort(key=lambda x: x[2])


def find_root(x):
    if root[x] != x:
        root[x] = find_root(root[x])
    return root[x]


result = 0
for s, d, v in info:
    s_root = find_root(s)
    d_root = find_root(d)
    if s_root != d_root:
        result += v
        if s_root < d_root:
            root[d_root] = s_root
        else:
            root[s_root] = d_root
print(result)
