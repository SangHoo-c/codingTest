import heapq
import sys

m, n = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(m)]
visited = [[-1 for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
heap = []
if arr[0][0] != -1:
    heapq.heappush(heap, [arr[0][0], 0, 0])
    visited[0][0] = arr[0][0]
else:
    print(-1)
    sys.exit()


while heap:
    cost, x, y = heapq.heappop(heap)
    for i in range(4):
        r = x + dx[i]
        c = y + dy[i]

        if 0 <= r < m and 0 <= c < n:
            if arr[r][c] != -1:
                if visited[r][c] == -1:
                    nex_cost = cost + arr[r][c]
                    visited[r][c] = nex_cost
                    heapq.heappush(heap, [nex_cost, r, c])

print(visited[-1][-1])
