# back tracking 적용 
# set, tuple = immutable 객체
# list = mutable 객체 
# set 을 정렬하기 위해선 list 로 변환 후, sorted 함수 사용 

import sys

N, M = map(int, input().split())

AList = list(sys.stdin.readline().strip().split(" "))  # 한줄 입력을 list 로 반환
vis = [0] * N       # 길이가 n 인 주어진 배열, 해당 idx 의 원소를 방문했는지 체크
arr = []            # 가능한 순열 (1개) list
rec = set()         # 가능한 순열 (M개) set


def promising(idx):
    if vis[idx] == 0:
        return True
    return False


def dfs(x):
    if x == M:
        rec.add(tuple(arr))     # set 에 list value 를 넣을 수 없다. list (mutable object) 이기 떄문에. 
        return
    else:
        for i in range(N):
            if promising(i):
                vis[i] = 1
                arr.append(int(AList[i]))
                dfs(x + 1)
                vis[i] = 0
                arr.pop()


dfs(0)
final = sorted(list(rec))    # set 을 정렬하기 위해 list 로 변환하고 sorted 한다.
for tup in final:
    for i in tup:
        print(i, end=" ")
    print()
