# 1. dp 를 매번 새로 그려주는 로직 
# 2. dfs 만 실행하는 로직 
# 모두 시간초과가 났다. 

# 3. dfs 와 dp 를 함께 실행하는 로직 
# => 시간 초과, dp를 잘 사용해야한다.
# 풀이를 찾아봄. visited 저장소를 사용하여, 필요하지 않은 계산을 줄인다. 

import sys
sys.setrecursionlimit(10000)

M, N = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
dp = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1
    
    # dp 의 핵심 
    # 방문한 경험이 있다면, 해당 저장소에 있는 값을 가져온다. 
    # why ? visited 가 필요한가 ? 
    # 방문을 했음에도 dp 의 값이 0 일 수 있기 때문에, visited 를 사용하여 방문 체크를 한다. 
    if visited[r][c]:
        return dp[r][c]
    
    visited[r][c] = 1

    dp[r][c] = 0
    for k in range(4):
        i = r + dx[k]
        j = c + dy[k]
        if 0 <= i < M and 0 <= j < N:
            if arr[i][j] < arr[r][c]:
                dp[r][c] += dfs(i, j)
    return dp[r][c]
    # 현재 좌표에서 더 이상 갈 수 있는 곳이 없다면, 반환한다. 



def main():
    print(dfs(0, 0))


main()
