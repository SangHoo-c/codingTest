# 라빈 카프 - Rolling Hash 방법
# KMP 와 마찬가지로 O(n) 으로 substring 을 해결할 수 있다. 
# 만약 hash function 이 좋지 못해서 충돌이 많이 일어날 경우, O(MN) 의 시간 복잡도가 나올 수도 있다. 
# hash function 을 잘 짜는게 중요. 


import sys

A = list(map(str, sys.stdin.readline().strip()))
B = list(map(str, sys.stdin.readline().strip()))

a_len = len(A)
b_len = len(B)

res = 0
_key = 0
for b in B:
    _key += ord(b)

_cmp = 0
for i in range(a_len - b_len + 1):
    if i == 0:
        for j in range(b_len):
            _cmp += ord(A[j])
    else:
        _cmp += ord(A[i + b_len - 1])

    if _cmp == _key:
        if A[i:i+b_len] == B:
            res = 1
            break
    _cmp -= ord(A[i])

print(res)



