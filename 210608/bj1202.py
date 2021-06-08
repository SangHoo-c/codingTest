# 문제를 제대로 읽지 않아 막혔다. 
# 가방에 최대 하나의 보석만이 들어갈 수 있다. 
# 가방의 크기가 작은 순서대로 가치가 높은 보석을 넣는다. 

import sys
import heapq


N, K = map(int, sys.stdin.readline().split())
jewel = []
bag = []

# 별도의 자료구조가 아니기떄문에, 사용시 빈 리스트를 넘겨줘야한다.
# heapq 모듈을 통해서 원소를 추가 / 삭제한 리스트가 최소 힙이다.

for _ in range(N):
    heapq.heappush(jewel, list(map(int, sys.stdin.readline().split())))
for _ in range(K):
    bag.append(int(sys.stdin.readline()))
# bag = [int(sys.stdin.readline()) for _ in range(K)]

bag.sort()

result = 0
candidate = []
for b in bag:
    while jewel and b >= jewel[0][0]:
        w, v = heapq.heappop(jewel)     # min-heapq 
        heapq.heappush(candidate, -v)   # candidate 를 max-heap 으로 만든다.
    if candidate:  
        result -= heapq.heappop(candidate)   # 가능한 보석중 가장 큰 가치를 가진 놈을 가방에 넣는다. 

print(result)
