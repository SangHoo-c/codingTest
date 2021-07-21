import sys, heapq

N = int(sys.stdin.readline())
l_heap = []  # max heap
r_heap = []  # min heap
for i in range(N):
    n = int(sys.stdin.readline())

    # 1. l_heap, r_heap 번갈아서 원소를 넣어준다.
    if i % 2 == 0:
        heapq.heappush(l_heap, -n)  # max heap
    else:
        heapq.heappush(r_heap, n)   # min heap

    # 2. l_heap 의 최댓값과 r_heap 의 최솟값을 비교한다.
    # l_heap 최댓값이 r_heap 보다 클 경우, swap 한다.
    if r_heap and - l_heap[0] > r_heap[0]:
        left_max = - heapq.heappop(l_heap)
        right_min = heapq.heappop(r_heap)

        heapq.heappush(l_heap, - right_min)
        heapq.heappush(r_heap, left_max)

    # swap 된 값 중에 문제의 조건에 맞는 답을 출력한다.
    print(- l_heap[0])
