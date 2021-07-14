# 1. tree 와 leaf 배열의 크기는 같다. 
# 2. num 을 이진수로 나타내었을때 마지막 1의 위치 = 해당 tree[num]에 담아야하는 수들의 합 
# 수를 1 ~ N 이라하자. 
# if leaf[12] = 4 이라면, tree[12] 에는 ( 12 - leaf[12] ~ 12 )  까지의 총 (leaf[12] = 4)개의 숫자의 합이 저장된다. 
# sum 은 마지막 1의 위치를 뺴주면서 게속 더해준다. 
# update 또한 마지막 1의 위치를 더해가며 부모의 값을 갱신해준다. 

# ref. https://www.acmicpc.net/blog/view/21


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

    # leaf 는 가장 밑단 노드 
    # tree 는 조상 노드
    leaf = [0] * (N + 1)
    tree = [0] * (N + 1)

    for i in range(1, N + 1):
        x = int(input())
        leaf[i] = x
        update(i, x)

    for i in range(M + K):
        a, b, c = map(int, sys.stdin.readline().split())
        # 1. update 과정이라면
        if a == 1:
            update(b, c - leaf[b])  # 바뀐 크기 c - leaf[b] 적용
            leaf[b] = c
        else:
            # b ~ c 구간 합 구하기 
            print(_sum(c) - _sum(b-1))
