# N <= 500,000 
# 모두 한번씩 수행해보는 브루스 포스 알고리즘 
# for #1  N <= 1,000,000 
# for #2 len <= 6
# O(N * len)

# 예외 1. 모든 숫자가 고장난 경우 
# 예외 2. 고장난 숫자가 없는 경우 

N = int(input())
M = int(input())

min_value = 1e9
enable = {str(i) for i in range(10)}


if M != 0:
    enable -= set(map(str, input().split()))  # 고장난 버튼 리스트 제거

    
for i in range(1000001):
    cnt = 0
    input_str = str(i)
    input_len = len(input_str)

    for j in range(input_len):
        if input_str[j] not in enable:
            break
        elif j == input_len - 1:
            min_value = min(min_value, abs(N - i) + input_len)

print(min(min_value, abs(N - 100)))
