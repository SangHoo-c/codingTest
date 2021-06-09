# dp 의 정석 
# 각 원소의 값을 기억하지 않고, 위치를 기억한다. 
# A(n-1) 과 A(n) 의 관계를 구한다. 

n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
