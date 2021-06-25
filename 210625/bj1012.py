import sys
sys.setrecursionlimit(100000)


# dfs 문제. 얼마나 깊이 들어갈지 계산하는데에 시간이 걸렸다. 
# 자신의 위치에서 가능하다면, + 1
# dfs 이니, 자신의 위치에서 나머지 4방향을 모두 돌린 값에, 자기자신 + 1 을 return 해주면 된다. 
def dfs(r, c):
    if 0 > r or r > N - 1 or 0 > c or c > M - 1:
        return 0
    if visited[r][c] or arr[r][c] != 1:
        return 0
    visited[r][c] = 1
    return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + 1

# input 으로 받은 arr 와 위치를 기억하는 visited 를 잘 사용해야한다. 
T = int(sys.stdin.readline().strip())
for _ in range(T):
    result_arr = []
    M, N, K = map(int, sys.stdin.readline().split(" "))
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, sys.stdin.readline().split(" "))
        arr[i][j] = 1
    
    # ele 값은 해당 dfs 를 모두 순회한 연속된 애벌레의 갯수. 
    # list 에 넣고 문제에서 원하는 총 길이를 구한다. 
    for r in range(N):
        for c in range(M):
            ele = dfs(r, c)
            if ele:
                result_arr.append(ele)

    print(len(result_arr))
