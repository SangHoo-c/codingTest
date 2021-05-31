# N <= 500,000 
# 모두 한번씩 수행해보는 브루스 포스 알고리즘 
# for #1  N <= 1,000,000 
# for #2 len <= 6
# O(N * len)

N = int(input())
M = int(input())

broken_btn = list(map(int, input().split()))
min_value = 1e9

for i in range(1000000):
    cnt = 0
    input_str = str(i)
    input_len = len(input_str)

    for j in range(input_len):
        if int(input_str[j]) not in broken_btn:
            cnt += 1

    if cnt == input_len:
        min_value = min(min_value, abs(N - i) + input_len)


print(min(min_value, abs(N - 100)))
