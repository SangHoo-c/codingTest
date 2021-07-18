import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split(" ")))
arr = sorted(arr)
print(arr, end="---")
used = [0] * N
chosen = []


# 정렬된 arr 배열
# 바로 이전 원소와 비교하여 중복되는 값이 있는 경우를 체크하기 위해
# 1. arr의 첫 원소
# 2. arr 의 이전 원소와 겹치지 않는다.
# 3. 이전 원소와 겹치는 경우, ex) '..11..' 인 경우, 두번째 1을 사용하기 위해선,첫번째 1이 체크된 이후에 쓸 수 있다.  
# 첫번째 원소가 체크된 이후에야 쓸 수 있다. => sorted 되어 있는 상태 이기 때문에,
# used[x-1] 에 0 이 아닌 값이 있는 경우
 

def promising(x):
    # if used[x] == 0:
    if used[x] == 0 and (x == 0 or arr[x - 1] != arr[x] or used[x - 1]):
        return True
    else:
        return False


def dfs(x):
    # 2.
    if x == N:
        print(chosen)
        return

    # 3.
    for i in range(N):
        if promising(i):
            chosen.append(arr[i])
            used[i] = 1
            dfs(x + 1)
            used[i] = 0
            chosen.pop()


dfs(0)
