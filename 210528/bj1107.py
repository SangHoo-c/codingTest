# 모든 경우를 시도해보는 방법 
# 5,000,000 * 7 번 실행되는 이중 for 문을 사용했다. 
# 코드의 개선이 필요함 

N = int(input())
C = int(input())
vis = list(map(int, input().split()))
min_str = "+119"
pre_min = 1e+9


for i in range(5000001):      
    cnt = 0
    num_str = str(i)

    for j in range(len(num_str)):
        if int(num_str[j]) not in vis:
           cnt += 1
    if cnt == len(num_str):
        if pre_min > abs(i-N):
            pre_min = abs(i-N)
            min_str = num_str
            
print(min(pre_min + len(min_str), abs(N-100)))
