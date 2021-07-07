# O(n^4) 복잡도를 줄이기 위해 
# 4 => 2 합쳐서 진행 
# O( n^2 ) 복잡도로 진행 가능 
# dict 를 사용할때, dict.get(key, default_value) 로 value 를 가져올 수 있다. => 적응하기 


import sys

n = int(input())
A, B, C, D = [], [], [], []

AB = {}
CD = {}
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


result = 0
for a in A:
    for b in B:
        AB[a + b] = AB.get(a + b, 0) + 1

for c in C:
    for d in D:
        # AB 딕셔너리에서 - (c + d) 값을 꺼내보고 없으면 0, 있다면 해당 value 값을 더한다.
        result += AB.get(-(c + d), 0)
print(result)
