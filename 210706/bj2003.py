# two - pointer 를 사용하면 시간복잡도를 줄일 수 있다. 
# O(n^2) => O(2*n)
import sys

N, M = map(int, input().split())
num = list(map(int, sys.stdin.readline().split(" ")))


def one_pointer():
    cnt = 0
    for i in range(N):
        sum = 0
        for j in range(i, N):
            sum += num[j]
            if sum == M:
                cnt += 1
                break
    print(cnt)


def two_pointer():
    count = 0
    interval_sum = 0
    end = 0

    # start를 차례대로 증가시키며 반복
    for start in range(N):
        # end를 가능한 만큼 이동시키기
        while interval_sum < M and end < N:
            interval_sum += num[end]
            end += 1
        # 부분합이 m일 때 카운트 증가
        if interval_sum == M:
            count += 1
        interval_sum -= num[start]

    print(count)


one_pointer()
two_pointer()
