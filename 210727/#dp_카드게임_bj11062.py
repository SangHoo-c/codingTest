import sys

sys.setrecursionlimit(10 ** 8)


def pick_card(turn, i, j):
    if i > j:
        return 0
    if dp[i][j]:
        return dp[i][j]

    # A, turn == True
    if turn:
        dp[i][j] = max(num[i] + pick_card(False, i + 1, j), pick_card(False, i, j - 1) + num[j])
        return dp[i][j]

    # B, turn == False
    if not turn:
        dp[i][j] = min(pick_card(True, i + 1, j), pick_card(True, i, j - 1))
        return dp[i][j]


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split(" ")))
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # 초기화
    # for i in range(N):
    #     dp[i][i] = num[i]
"""
  해당 부분이 필요 없는 이유, 
  dp[i][j] = A 기준으로 뽑는 최댓값, B에 대한 값은 저장하지 않는다. 
  따라서 dp 를 출력해보면, 
  [[0, 2, 2, 6, 0], [0, 0, 5, 5, 0], [0, 0, 0, 5, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
  이렇게 반복되는 값이 나온다. 
  이는 B 차례에서 자신이 뽑는 값을 저장하지 않고 
  다음 A가 뽑은 최솟값을 저장함으로, B 입장에선 최선의 선택을 했기 떄문이다. 
"""
    
    # for i in range(N - 1):    
    #     dp[i][i + 1] = max(num[i], num[i + 1])

    pick_card(True, 0, N - 1)
    # print(dp)
    print(dp[0][N - 1])
