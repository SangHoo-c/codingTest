# 자릿수를 기억하는 포인트 
# greedy 로 풀었다. 
# 브루스 포스 방법도 가능해 보임. 

import sys
N = int(input())
arr = []    # 입력으로 받은 문자열 리스트
dic = {}    # 입력으로 받은 문자열의 자리수를 나타내는 딕셔너리

for i in range(N):
    a = str(sys.stdin.readline().strip())
    arr.append(a)


for num in arr:     # num 은 문자열 한개, ex) ABC
    num_len = len(num)
    for n in num:   # n 은 num 문자열을 이루는 단어 한개, ex) A
        if n in dic:
            dic[n] += pow(10, num_len-1)
        else:
            dic[n] = pow(10, num_len-1)
        num_len -= 1

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# sorted(dic, key=dic.values())

# print(dic)
mul = 9
anw = 0
for num in dic:
    anw += num[1] * mul
    mul -= 1
print(anw)
