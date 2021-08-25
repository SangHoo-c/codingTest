"""
  효율성 문제
  1. A 를 sort 한다.
  2. 원소간의 차를 구한다. 
  
  => O(N*logn(N)) 으로 처리 가능 : 정렬 알고리즘
"""

def solution(A):
    A.sort()
    B = [0] * (len(A) - 1)
    for i in range(len(A)-1):
        B[i] = A[i+1] - A[i]
    
    res = 0
    for i in range(1, len(B)):
        if A[i - 1] > B[i]:
            res = 1
            break
    
    return res
