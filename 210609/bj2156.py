# case1 : o o 
# case2 : x o
# case3 : o x

# 헷갈렸던 부분은 A(n-2), A(n-1), A(n) 을 넘어 
# A(n-3) 에 원소가 어떤게 선택되었을지 고민했던 점이었다. 

# dp 의 핵심은 규칙 찾기이다. 
# 해당 규칙이 점화식으로 돌아가는 것만 생각하자. 

n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0, w[1]]
if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
print(dp[n])
