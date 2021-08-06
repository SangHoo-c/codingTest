"""
1. dfs 로 조합을 먼저 생각했음 
=> 모든 케이스를 다 해보는 풀이, 시간초과 
2. dp 로 해결 
"""

def solution(land):
    N = len(land)
    M = len(land[0])
    dp = [[0 for _ in range(4)] for _ in range(N)]
    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(1, N):
        for j in range(4):
            _max = -1
            for k in range(4):
                if j == k:
                    continue
                _max = max(_max, dp[i-1][k])
            dp[i][j] = land[i][j] + _max

    return max(dp[N-1])
