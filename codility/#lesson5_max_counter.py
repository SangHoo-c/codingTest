"""
  1 <= N <= 100,000
  1 <= M <= 100,000   # A 의 길이
  
  O(N^2) 풀이는 불가능하다. 
  O(2 * N) 으로 해결함. 
  
"""

def solution(N, A):
    counter = [0] * (N + 1) 
    _prv_max = 0
    _cur_max = 0
    for a in A:
        if a == N + 1:
            _prv_max = _cur_max
            continue

        if counter[a] <= _prv_max:
            counter[a] = _prv_max + 1
        else:
            counter[a] += 1
        
        _cur_max = max(_cur_max, counter[a])

    for i in range(1, N+1):
        if counter[i] <= _prv_max:
            counter[i] = _prv_max
    
    return counter[1:]
