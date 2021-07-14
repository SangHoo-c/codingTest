import sys


# i 번째 수까지 누적합을 계산 하는 함수
def _sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 0 이 아닌 비트만큼 빼가면서 이동
        i -= (i & -i)
    return result


# i 번째 수를 dif 만큼 더하는 함수
# 0 이 아닌 비트만큼 더해가면서 상위 조상들의 값을 갱신해준다.
def update(i, dif):
    while i <= N:
        tree[i] += dif
        i += (i & -i)


if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().split())

    # arr 는 가장 밑단의 leaf
    # tree 는 조상 노드
    arr = [0] * (N + 1)
    tree = [0] * (N + 1)

    for i in range(1, N + 1):
        x = int(input())
        arr[i] = x
        update(i, x)

    for i in range(M + K):
        a, b, c = map(int, sys.stdin.readline().split())
        # 1. update 과정이라면
        if a == 1:
            update(b, c - arr[b])  # 바뀐 크기 c - arr[b] 적용
            arr[b] = c
        else:
            # b ~ c 구간 합 구하기 
            print(_sum(c) - _sum(b-1))
