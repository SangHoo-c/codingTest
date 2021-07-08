# 가방에는 최대 한개의 보석만 넣을 수 있다. 
# 우선순위큐 => 넣자마자 정렬. O(nlogn) 
# deque, 별개의 자료구조 사용 => 정렬한 다음에 계산. O(nlogn)
# 같은 방법이지만, 더 편하게 수행, 사고도 해볼 수 있다. 
# 다익스트라에도 사용된다. 

import sys
import heapq

N, K = map(int, sys.stdin.readline().split(" "))
jew = list(list(map(int, sys.stdin.readline().split(" "))) for _ in range(N))
bag = list(int(sys.stdin.readline()) for _ in range(K))

jew.sort()
bag.sort()

heap = []
_max = 0

for b in bag:
    while jew and b >= jew[0][0]:  # 가방보다 작은 경우, 모두 넣어준다.
        heapq.heappush(heap, -jew[0][1])  # 무게를 기준으로 max heap 생성
        heapq.heappop(jew)  # 가장 앞에 있는 원소를 삭제
    print(heap)
    if heap:
        _max += heapq.heappop(heap)
    elif not jew:     # 보석이 더 이상 없다면 할 필요는 없다.
        break

print(-_max)
